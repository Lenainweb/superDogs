from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'registration_of_dogs/index.html')
