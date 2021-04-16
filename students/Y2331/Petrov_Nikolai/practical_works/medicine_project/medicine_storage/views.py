from django.contrib import auth
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, mixins, generics

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

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class ManufacturersList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class ManufacturerView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return models.Manufacturer.objects.get(pk=pk)
#         except models.Manufacturer.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = serializers.ManufacturerSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = serializers.ManufacturerSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
