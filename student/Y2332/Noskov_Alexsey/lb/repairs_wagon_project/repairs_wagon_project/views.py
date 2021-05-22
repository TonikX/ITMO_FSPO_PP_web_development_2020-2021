from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

def redirect_blog(request):
    return redirect('worker_l', permanent=True)

