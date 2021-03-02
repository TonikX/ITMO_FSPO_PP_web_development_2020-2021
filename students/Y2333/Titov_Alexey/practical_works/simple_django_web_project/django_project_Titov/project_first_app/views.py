from django.http import Http404
from django.shortcuts import render

from .models import Owner

# Create your views here.

def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner/detail.html', {'owner': o})
