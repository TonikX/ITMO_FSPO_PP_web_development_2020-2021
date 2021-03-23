from django.shortcuts import render
from django.http import Http404
from blog_first_app.models import Owner
def detail(request, id):
    try:
        p = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'detail.html', {'Owner': p})

# Create your views here.
