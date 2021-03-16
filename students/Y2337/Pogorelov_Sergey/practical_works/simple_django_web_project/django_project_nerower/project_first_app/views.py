from django.shortcuts import render
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from project_first_app.models import Owner, Car


def home(request):
    return render(request, 'home.html')

def owner_info(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    
    return render(request, 'owner.html', {"owner": owner})

def owner_list(request):
    context = {}
    context["owner_list"] = Owner.objects.all()

    return render(request, "owner_list.html", context)


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = 'car_list_view.html'

    def get_queryset(self):
        owner = self.request.GET.get('owner')

        if owner:

            try:
                owner = int(owner)
                queryset = self.queryset.filter(owner=owner)
            
            except ValueError:
                queryset = self.model.objects.none()
    
        return queryset

class CarRetrieveView(DetailView):
    model = Car
