from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from .models import AboutUs, RegistrationExhibition
from .forms import RegistrationExhibitionForm

class HomePageView(TemplateView):
    
    def get(self, request, **kwargs):
        date = AboutUs.objects.last()
        # if request.LANGUAGE_CODE == 'ru':
        #     test = "OK"
        # else:
        test = request.LANGUAGE_CODE
        return render(request, 'registration_of_dogs/index.html', context = {'title' : date.title, 'content': _(date.content), 'test': test})


class RegistrationExhibitionView(TemplateView):
    
    def get(self, request, **kwargs):
        
        form = RegistrationExhibitionForm()
        return render (request, 'registration_of_dogs/registration_exhibition.html', context = {'form': form})
        
    def post(self, request, **kwards):    
        
        form = RegistrationExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            pass
        

    # date = RegistrationExhibition.objects()
    # print (date.title)
    # return render(request, 'registration_of_dogs/registration_exhibition.html')#, context = {'title' : date.title, 'content': date.content})

