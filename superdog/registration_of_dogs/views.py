from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import AboutUs, RegistrationExhibition
from .forms import RegistrationExhibitionForm

class HomePageView(TemplateView):
    
    def get(self, request, **kwargs):
        date = AboutUs.objects.last()
        # print (date.title)
        return render(request, 'registration_of_dogs/index.html', context = {'title' : date.title, 'content': date.content})


class RegistrationExhibitionView(TemplateView):
    
    def get(self, request, **kwargs):
        
        form = RegistrationExhibitionForm()
        return render (request, 'registration_of_dogs/registration_exhibition.html', context = {'form': form})
        
    def post(self, request, **kwards):    
        
        form = RegistrationExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            pass
        

    # date = RegistrationExhibition.objects()
    # print (date.title)
    # return render(request, 'registration_of_dogs/registration_exhibition.html')#, context = {'title' : date.title, 'content': date.content})

