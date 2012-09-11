from django.http import HttpResponse
from django.shortcuts import render

from hobbies.models import *
from hobbies.forms import HobbyForm

def list(request):
    if request.POST:
        form = HobbyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = HobbyForm()

    hobbies = Hobby.objects.all()
    return render(request, 'hobbies.html', {
        'hobbies': hobbies,
        'form': form,
        })
