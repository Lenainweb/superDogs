from django.shortcuts import render

from .models import AboutUs

# Create your views here.

def index(request):
    date = AboutUs.objects.last()
    # print (date.title)
    return render(request, 'registration_of_dogs/index.html', context = {'title' : date.title, 'content': date.content})
