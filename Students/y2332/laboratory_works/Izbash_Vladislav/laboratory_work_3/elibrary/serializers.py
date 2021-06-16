from typing import Type

import django.db.models
from rest_framework import serializers


def create_serializer(model: Type[django.db.models.Model]):
    return type(
        model.__name__ + 'Serializer',
        (serializers.ModelSerializer,),
        {
            "Meta": type("Meta", (), {
                "model": model,
                "fields": "__all__",
                "read_only_fields": ["id"],
            }),
        },
    )