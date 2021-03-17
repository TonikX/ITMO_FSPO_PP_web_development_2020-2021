from django.shortcuts import render
from django.http import Http404
from blog.models import CarOwner


def detail(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    print(p)
    return render(request, 'Owner/detail.html', {'Owner': p})
