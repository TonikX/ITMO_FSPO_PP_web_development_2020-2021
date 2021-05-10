import encodings.utf_8
import re
from functools import reduce
from typing import Type, overload

from django.contrib.auth import decorators
from django.db.models import Model, Field, CharField, TextField
from django.db.models.fields.related_descriptors import ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor
from django.db.models.query_utils import DeferredAttribute, Q
from django.forms import ModelForm
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from stringcase import snakecase, sentencecase


def replace_by(s: str, replaces: dict):
    for old, new in replaces.items():
        s = s.replace(old, str(new))
    return s

def _get_template(path, mapped_fields={}, **replaces):
    template = open(path, 'r', encoding='utf-8').read()
    template = replace_by(template, mapped_fields)
    for old, new in replaces.items():
        template = template.replace(f'@{old}', str(new))
    return template

def _get_class(name, *bases, **fields):
    return type(name, bases, fields)

class ViewGenerator:
    def __init__(self, model: Type[Model], fields=None, root_path='/'):
        self.list_view = None
        self.create_view = None
        self.delete_view = None
        self.detail_view = None
        self.search_view = None

        self.__name__ = model.__name__

        self.mapped_fields = {
            '@root_path': root_path
        }

        self.model = model
        if fields is None:
            self.fields = list(
                map(
                    lambda t: t[0],
                    filter(
                        lambda t: (isinstance(t[1], DeferredAttribute)
                                  and not isinstance(t[1], ForeignKeyDeferredAttribute)) or isinstance(t[1], ForwardManyToOneDescriptor),
                        self.model.__dict__.items()
                    )
                )
            )
        else:
            self.fields = fields

        class GeneratedForm(ModelForm):
            class Meta:
                model = self.model
                fields = self.fields

        self.form = GeneratedForm

    def generate_delete_view(self, user_groups=(), login_required=False, success_url='@root_path/list', *args, **kwargs):
        success_url = replace_by(success_url, self.mapped_fields)

        if self.delete_view is None:
            model_name = snakecase(self.model.__name__)

            template = _get_template(
                'templates/delete_view.html', self.mapped_fields,
                name=sentencecase(self.model.__name__).lower(), **kwargs
            )

            template_name = f'{model_name}_delete_view.html'
            open(f'templates/{template_name}', 'wb').write(template.encode('utf-8'))

            self.delete_view = _get_class(
                'GeneratedDeleteView', DeleteView,
                success_url=success_url, model=self.model,
                template_name=template_name
            ).as_view()

            if login_required:
                self.delete_view = decorators.login_required(self.delete_view)

            for user_group in user_groups:
                self.delete_view = decorators.user_passes_test(lambda user: user.groups.filter(name=user_group).exists())(
                    self.delete_view)

        return self.delete_view

    def generate_create_view(self, user_groups=(), login_required=False, success_url='@root_path/list', *args, **kwargs):
        success_url = replace_by(success_url, self.mapped_fields)

        if self.create_view is None:
            model_name = snakecase(self.model.__name__)

            template = _get_template(
                'templates/create_view.html', self.mapped_fields,
                name=sentencecase(self.model.__name__).lower(), **kwargs
            )

            template_name = f'{model_name}_create_view.html'
            open(f'templates/{template_name}', 'w').write(template)

            self.create_view = _get_class(
                'GeneratedCreateView', CreateView,
                success_url=success_url, model=self.model,
                fields=self.fields, template_name=template_name
            ).as_view()

            if login_required:
                self.create_view = decorators.login_required(self.create_view)

            for user_group in user_groups:
                self.create_view = decorators.user_passes_test(lambda user: user.groups.filter(name=user_group).exists())(self.create_view)

        return self.create_view

    def generate_list_view(self, user_groups=(), login_required=False, paginate_by=10, *args, **kwargs):
        if self.list_view is None:
            model_name = snakecase(self.model.__name__)

            template = _get_template(
                'templates/list_view.html', self.mapped_fields,
                name=sentencecase(self.model.__name__).lower(), fields='\n'.join([
                    '<li>{{ object.@field }}</li>'.replace('@field', field)
                    for field in self.fields
                ]), **kwargs
            )

            template_name = f'{model_name}_list_view.html'
            open(f'templates/{template_name}', 'w').write(template)

            self.list_view = _get_class(
                'GeneratedListView', ListView,
                model=self.model, template_name=template_name, paginate_by=paginate_by
            ).as_view()

            if login_required:
                self.list_view = decorators.login_required(self.list_view)

            for user_group in user_groups:
                self.list_view = decorators.user_passes_test(lambda user: user.groups.filter(name=user_group).exists())(self.list_view)

        return self.list_view

    def generate_detail_view(self, user_groups=(), login_required=False, *args, **kwargs):
        if self.detail_view is None:
            model_name = snakecase(self.model.__name__)

            template = _get_template(
                'templates/detail_view.html', self.mapped_fields,
                name=sentencecase(self.model.__name__).lower(), **kwargs,
            )

            template_name = f'{model_name}_detail_view.html'
            open(f'templates/{template_name}', 'w').write(template)

            self.detail_view = _get_class(
                'GeneratedDetailView', DetailView,
                model=self.model, template_name=template_name
            ).as_view()

            if login_required:
                self.detail_view = decorators.login_required(self.detail_view)

            for user_group in user_groups:
                self.detail_view = decorators.user_passes_test(lambda user: user.groups.filter(name=user_group).exists())(self.detail_view)

        return self.detail_view

    def generate_search_view(self, paginate_by_=10, **kwargs):
        if self.search_view is None:
            model_name = snakecase(self.model.__name__)

            template = _get_template(
                'templates/list_view.html', self.mapped_fields,
                title="Search results", fields='\n'.join([
                    '<li>{{ object.@field }}</li>'.replace('@field', field)
                    for field in self.fields
                ]), **kwargs
            )

            template_name_ = f'{model_name}_search_view.html'
            open(f'templates/{template_name_}', 'w').write(template)

            class GeneratedSearchResultView(ListView):
                model = self.model
                template_name = template_name_
                paginate_by = paginate_by_
                fields = self.fields

                def get_queryset(self, *args, **kwargs):
                    val = self.request.GET.get("q")
                    if val:
                        queryset = self.model.objects.filter(
                            reduce(Q.__or__, map(lambda key: Q(**{key: val}), [f'{field}__icontains' for field in self.fields]))
                        ).distinct()
                    else:
                        queryset = self.model.objects.none()
                    return queryset

            self.search_view = GeneratedSearchResultView

        return self.search_view.as_view()

def generate_views(model: Type[Model]) -> ViewGenerator:
    return ViewGenerator(model)

def generate_views(root_path=None, fields=None):
    def wrapper(model: Type[Model]) -> ViewGenerator:
        if root_path is None:
            return ViewGenerator(model, fields=fields)
        return ViewGenerator(model, fields=fields, root_path=root_path)
    return wrapper

class generate_to_str:
    def __init__(self, fields=None, pattern=None):
        self.fields = fields
        self.pattern = pattern

    @staticmethod
    def from_pattern(pattern):
        return generate_to_str(pattern=pattern)

    @staticmethod
    def from_fields(fields):
        return generate_to_str(fields=fields)

    def __call__(self, model: Type[Model]):
        if self.pattern is not None:
            fields = re.findall(r'\@[A-Za-z0-9_]+', self.pattern)

            def __str__(_self):
                return replace_by(self.pattern, {s: getattr(_self, s[1:]) for s in fields})

            model.__str__ = __str__
            return model

        elif self.fields is None:
            self.fields = list(
                map(
                    lambda t: t[0],
                    filter(
                        lambda t: isinstance(t[1], DeferredAttribute),
                        model.__dict__.items()
                    )
                )
            )

        def __str__(_self):
            return str('\n'.join([f'{field} : {getattr(_self, field)}' for field in self.fields]))
        model.__str__ = __str__
        return model



