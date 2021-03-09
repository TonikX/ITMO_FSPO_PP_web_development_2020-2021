from django.shortcuts import render
from django.shortcuts import Http404
from project_first_app.models import Owner


def owner(request, owner_id):
    try:
        selected_owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'owner': selected_owner})
