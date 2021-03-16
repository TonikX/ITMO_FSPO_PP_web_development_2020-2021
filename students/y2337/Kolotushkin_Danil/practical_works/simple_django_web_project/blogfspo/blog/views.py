from django.shortcuts import render
from django.http import Http404 
from django.shortcuts import render
from blog.models import owner
def detail(request, poll_id):
    try: 
        p = owner.objects.get(pk=poll_id)
    except owner.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'owner.html', {'owner': p}) 

