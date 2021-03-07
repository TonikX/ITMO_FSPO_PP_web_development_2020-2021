from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner


# Create your views here.
def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'Owner.html', {'Owner': p})
