from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
from project_first_app.models import Owner



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def ownerinfo(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})
