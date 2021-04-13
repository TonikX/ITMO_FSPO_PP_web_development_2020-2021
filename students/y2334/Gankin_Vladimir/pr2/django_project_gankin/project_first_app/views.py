# # Create your views here.
# from django.http import Http404
# from django.shortcuts import render
#
from django.http import Http404
from django.shortcuts import render

from project_first_app.models import AutoOwner
from project_first_app.models import Auto


def owner(request, owner_id):
    try:
        owner = AutoOwner.objects.get(pk=owner_id)
        print('Owner:', owner)
    except AutoOwner.DoesNotExist:
        raise Http404('Auto owner does not exist')
    return render(request, 'owner.html', {'owner': owner})


def auto(request, auto_id):
    try:
        auto = Auto.objects.get(pk=auto_id)
        print('Auto:', auto)
    except Auto.DoesNotExist:
        raise Http404('Auto does not exist')
    return render(request, 'auto.html', {'auto': auto})
