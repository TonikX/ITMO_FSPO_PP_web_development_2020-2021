from django.shortcuts import render
from django.http import Http404
from blog.models import autoOwner

def detail(request, id):
    try:
        p = autoOwner.objects.get(pk=id)
    except autoOwner.DoesNotExist:
        raise Http404("autoOwner does not exist")
    return render(request, 'detail.html', {'autoOwner': p})

# Create your views here.
