import re
from collections import namedtuple
from dataclasses import dataclass
from functools import reduce
from typing import Type

from django.contrib.auth import decorators
from django.db.models import Model
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor
from django.db.models.query_utils import DeferredAttribute, Q
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from stringcase import snakecase


def replace_by(s: str, replaces: dict):
    for old, new in replaces.items():
        s = s.replace(old, str(new))
    return s


class ViewGenerator:
    @dataclass
    class Field:
        name: str
        type: object
        is_foreign: bool
        value: object = None

        def set(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
            return self

    def __init__(self, model: Type[Model], fields=None, root_path='/'):
        self.list_view = None
        self.create_view = None
        self.delete_view = None
        self.detail_view = None
        self.search_view = None
        self.update_view = None

        self.__name__ = model.__name__

        self.mapped_fields = {
            'root_path': root_path,

        }
        self.connections = []

        self.model = model
        if fields is None:
            self.fields = list(
                map(
                    lambda t: ViewGenerator.Field(
                        name=t[0],
                        type=t[1],
                        is_foreign=isinstance(t[1], ForwardManyToOneDescriptor)
                    ),
                    filter(
                        lambda t: (isinstance(t[1], DeferredAttribute)
                                   and not isinstance(t[1], ForeignKeyDeferredAttribute))
                                  or isinstance(t[1], ForwardManyToOneDescriptor),
                        self.model.__dict__.items()
                    )
                )
            )
        else:
            self.fields = fields

        self.field_names = list(map(lambda field: field.name, self.fields))

    def _generate_view(
            self, base: Type[View],
            base_template_name, login_required=False,
            name=None, user_groups=(),
            class_fields={}, custom_context_f=lambda _: {}, **extra_context
    ) -> View:

        model_name = self.model.__name__.lower() if name is None else name

        class GeneratedView(base):
            model = self.model
            template_name = base_template_name

            def get_context_data(view, **kwargs):
                context = super(GeneratedView, view).get_context_data(**kwargs)
                context = {
                    **context,
                    **self.mapped_fields,
                    **extra_context,
                    **custom_context_f(view),
                    'model_name': model_name
                }

                return context

        for name, value in class_fields.items():
            setattr(GeneratedView, name, value)

        view = GeneratedView.as_view()

        if login_required:
            view = decorators.login_required(view)

        for user_group in user_groups:
            view = decorators.user_passes_test(
                lambda user: user.groups.filter(name=user_group).exists()
            )(view)

        return view

    def generate_delete_view(self, success_url_postfix='list', **kwargs):
        if self.delete_view is None:
            self.delete_view = self._generate_view(
                base=DeleteView,
                base_template_name='delete_view.html',
                class_fields={'success_url': f"{self.mapped_fields['root_path']}/{success_url_postfix}"},
                cancel_url=self.mapped_fields['root_path'] + success_url_postfix,
                **kwargs
            )

        return self.delete_view

    def generate_create_view(self, success_url_postfix='list', **kwargs):
        if self.create_view is None:
            self.create_view = self._generate_view(
                base=CreateView,
                base_template_name='create_view.html',
                class_fields={
                    'success_url': f"{self.mapped_fields['root_path']}/{success_url_postfix}",
                    'fields': self.field_names
                }, **kwargs
            )

        return self.create_view

    def generate_list_view(self, paginate_by=10, **kwargs):
        if self.list_view is None:
            self.list_view = self._generate_view(
                base=ListView,
                base_template_name='list_view.html',
                class_fields={'paginate_by': paginate_by}, **kwargs
            )

        return self.list_view

    def generate_detail_view(self, **kwargs):
        if self.detail_view is None:
            def custom_context(view: DetailView):
                obj = view.get_object()
                Foreign = namedtuple('Foreign', ['model_name', 'id', 'to_one'])

                _custom_context = {
                    'fields': [
                        field.set(
                            value=getattr(obj, field.name)
                        )
                        if not field.is_foreign
                        else field.set(
                            value=Foreign(
                                model_name=field.type.field.related_model.__name__.lower(),
                                id=getattr(obj, field.type.field.related_model.__name__.lower() + '_id'),
                                to_one=getattr(obj, field.type.field.related_model.__name__.lower()),
                        ))
                        for field in self.fields
                    ],
                    'connections': []
                }

                for connection in self.connections:
                    connection_objects = connection.using.objects.all().filter(
                        Q(**{snakecase(view.model.__name__) + '_id': obj.id})
                    )

                    for i in range(len(connection_objects)):
                        connection_objects[i].model_name = connection.using.__name__.lower()
                        connection_objects[i].connected_model_name = connection.to_one.__name__.lower()
                        connection_objects[i].connected_object_id = \
                            getattr(connection_objects[i], snakecase(connection.to_one.__name__) + '_id')

                    _custom_context['connections'] += connection_objects

                return _custom_context

            self.detail_view = self._generate_view(
                DetailView, 'detail_view.html',
                custom_context_f=custom_context, **kwargs
            )

        return self.detail_view

    def generate_search_view(self, paginate_by=10, **kwargs):
        if self.search_view is None:
            def get_queryset(search_view, **_kwargs):
                val = search_view.request.GET.get("q")
                if val:
                    queryset = search_view.model.objects.filter(
                        reduce(Q.__or__,
                               map(lambda key: Q(**{key: val}),
                                   [f'{field}__icontains' for field in search_view.fields]))
                    ).distinct()
                else:
                    queryset = search_view.model.objects.none()
                return queryset

            self.search_view = self._generate_view(
                base=ListView,
                base_template_name='search_view.html',
                class_fields={
                    'get_queryset': get_queryset,
                    'fields': self.field_names,
                    'paginate_by': paginate_by
                }, **kwargs
            )

        return self.search_view

    def generate_update_view(self, success_url_postfix='list', **kwargs):
        if self.update_view is None:
            self.update_view = self._generate_view(
                base=UpdateView,
                base_template_name='update_view.html',
                class_fields={
                    'success_url': f"{self.mapped_fields['root_path']}/{success_url_postfix}",
                    'fields': self.field_names
                }, **kwargs
            )

        return self.update_view


def generate_views(root_path='/', fields=None):
    def wrapper(model: Type[Model]) -> ViewGenerator:
        return ViewGenerator(model, fields=fields, root_path=root_path)

    return wrapper


class generate_to_str:
    def __init__(self, fields=None, pattern=None):
        self.field_names = fields
        self.pattern = pattern

    @classmethod
    def from_pattern(cls, pattern):
        return cls(pattern=pattern)

    @classmethod
    def from_fields(cls, fields):
        return cls(fields=fields)

    def __call__(self, model: Type[Model]):
        if self.pattern is not None:
            fields = re.findall(r'\@[A-Za-z0-9_]+', self.pattern)

            def __str__(_self):
                return replace_by(self.pattern, {s: getattr(_self, s[1:]) for s in fields})

            model.__str__ = __str__
            return model

        elif self.field_names is None:
            self.field_names = list(
                map(
                    lambda t: t[0],
                    filter(
                        lambda t: isinstance(t[1], DeferredAttribute),
                        model.__dict__.items()
                    )
                )
            )

        def __str__(_self):
            return str('\n'.join([f'{field} : {getattr(_self, field)}' for field in self.field_names]))

        model.__str__ = __str__
        return model


@dataclass
class Connection:
    using: Type[Model]
    to_one: Type[Model]


def one_to_one(one: ViewGenerator, to_one: ViewGenerator):
    def wrapper(this: Type[Model]):
        one.connections.append(
            Connection(this, to_one.model)
        )
        to_one.connections.append(
            Connection(this, one.model)
        )

        return this

    return wrapper
