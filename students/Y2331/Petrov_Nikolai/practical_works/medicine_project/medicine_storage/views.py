from django.contrib import auth
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from rest_framework import mixins, generics, permissions, status
import medicine_storage.forms as forms

from . import models, serializers

success_url = '/index/'


def index(request):
    if request.user.is_authenticated:
        return render(request, '../dist/index.html')
    else:
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = auth_forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('index')
        else:
            print(form, form.is_valid())
    else:
        form = auth_forms.UserCreationForm()
    return render(request, 'auth/user_form.html', {'form': form})


class UsersList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ActiveSubstanceUpdate(UpdateView):
    model = models.ActiveSubstance
    form_class = forms.ActiveSubstanceForm
    success_url = success_url


class ActiveSubstanceCreate(CreateView):
    model = models.ActiveSubstance
    form_class = forms.ActiveSubstanceForm
    success_url = success_url


class ActiveSubstanceDelete(DeleteView):
    model = models.ActiveSubstance
    success_url = success_url


class ActiveSubstancesList(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = models.ActiveSubstance.objects.all()
    serializer_class = serializers.ActiveSubstanceSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ManufacturerUpdate(UpdateView):
    model = models.Manufacturer
    form_class = forms.ManufacturerForm
    success_url = success_url


class ManufacturerCreate(CreateView):
    model = models.Manufacturer
    form_class = forms.ManufacturerForm
    success_url = success_url


class ManufacturerDelete(DeleteView):
    model = models.Manufacturer
    success_url = success_url


class ManufacturersList(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ItemUpdate(UpdateView):
    model = models.Item
    form_class = forms.ItemForm
    success_url = success_url


class ItemCreate(CreateView):
    model = models.Item
    form_class = forms.ItemForm
    success_url = success_url


class ItemDelete(DeleteView):
    model = models.Item
    success_url = success_url


class ItemsList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UnitUpdate(UpdateView):
    model = models.Unit
    form_class = forms.UnitForm
    success_url = success_url


class UnitCreate(CreateView):
    model = models.Unit
    form_class = forms.UnitForm
    success_url = success_url


class UnitDelete(DeleteView):
    model = models.Unit
    success_url = success_url


class UnitsList(mixins.ListModelMixin,
                generics.GenericAPIView):
    serializer_class = serializers.UnitSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Unit.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
