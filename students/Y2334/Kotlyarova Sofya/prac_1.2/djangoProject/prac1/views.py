from django.http import Http404
from django.shortcuts import render
from prac1.models import Owner


def detail(request, id):
    try:
        o = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner/detail.html', {'owner': o})
