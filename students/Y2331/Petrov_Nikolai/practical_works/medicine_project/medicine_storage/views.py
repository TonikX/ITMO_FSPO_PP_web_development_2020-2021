from django.contrib import auth
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import mixins, generics

from . import models, serializers


def signup(request):
    if request.method == 'POST':
        form = auth_forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('home')
    else:
        form = auth_forms.UserCreationForm()
    return render(request, 'auth/user_form.html', {'form': form})


class UsersList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ActiveSubstancesList(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    queryset = models.ActiveSubstance.objects.all()
    serializer_class = serializers.ActiveSubstanceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ManufacturersList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemsList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UnitsList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    serializer_class = serializers.UnitSerializer

    # queryset = models.Unit.objects.all()

    def get_queryset(self):
        user = self.request.user
        print(user)
        return models.Unit.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
