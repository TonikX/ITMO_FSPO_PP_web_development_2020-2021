from typing import Type

import django.db.models
from rest_framework import viewsets

from .serializers import create_serializer


def create_view(model: Type[django.db.models.Model], search_fields: [str] = []):
    return type(
        model.__name__ + 'View',
        (viewsets.ModelViewSet,),
        {
            'serializer_class': create_serializer(model),
            'queryset': model.objects.all(),
            'search_fields': search_fields,
        },
    )
