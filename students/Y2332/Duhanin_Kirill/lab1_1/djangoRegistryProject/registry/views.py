# from django.shortcuts import render
# from .models import *
# from django.views.generic import *
#
#
# def without_sys(lst):
#     return filter(lambda s: s[0][:2] != '__' and s[0][-2:] != '__', lst)
#
# def without_foreign_id(lst):
#     return filter(lambda field: not isinstance(field, ForeignKey) and not field.primary_key, lst)
#
#
# # (('address', 'name'), ('name', 'boss', 'phone', 'type'), ('name', 'phone'), ('start_date', 'end_date'),
# #      ('code', 'target'), ('start_date', 'end_date'), ('name', 'cost', 'standard_code'), ('')
# #     )
#
# models = dict(list(without_sys(Models.__dict__.items())))
#
# for (name, model) in zip(
#     models.items(), map(without_foreign_id, without_sys(models.values().__dict__.items()))
# ):
#     for view in ('CreateView', 'UpdateView', 'ListView', 'RetrieveView', 'DeleteView'):
from django.db.models import *
from .models import *
from django.views.generic import ListView


class CardView(ListView):
    template_name = 'home.html'
    model = CardModel




