# Create your views here.
from datetime import datetime

from django.http import Http404

from django.shortcuts import render
from nmstr1.models import Car_owner



def example_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)

def detail(request, owner_id):
    try:
        owner = Car_owner.objects.get(pk=owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'index.html', {'owner': owner})


