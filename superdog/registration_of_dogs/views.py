from django.forms import formsets
from django.shortcuts import redirect, render

from .models import AboutUs, RegistrationExhibition
from .forms import RegistrationExhibitionForm

# Create your views here.

def index(request):
    date = AboutUs.objects.last()
    # print (date.title)
    return render(request, 'registration_of_dogs/index.html', context = {'title' : date.title, 'content': date.content})


def registration_exhibition(request):
    registration_exhibition_form = RegistrationExhibitionForm()

    if request.method == 'POST':
            formset = registration_exhibition_form(request.POST)
            if formset.is_valid():
                formset.save()
                return redirect('')
    else:
        formset = registration_exhibition_form
    context = {'formset': formset}
    return render (request, 'registration_of_dogs/registration_exhibition.html', context)

    # date = RegistrationExhibition.objects()
    # print (date.title)
    # return render(request, 'registration_of_dogs/registration_exhibition.html')#, context = {'title' : date.title, 'content': date.content})

