from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from .models import AboutUs, RegistrationExhibition, Exebition
from .forms import RegistrationExhibitionForm

class HomePageView(TemplateView):
    
    def get(self, request, **kwargs):
        date = AboutUs.objects.last()
        
        test = request.LANGUAGE_CODE
        return render(request, 'registration_of_dogs/index.html', context = {'title' : date.title, 'content': _(date.content), 'test': test})


class RegistrationExhibitionView(TemplateView):
    
    def get(self, request, **kwargs):
        
        # data_of_exebition = Exebition.objects.filter(status_of_exebition = 1)
        # print([i.type_exebition for i in data_of_exebition])

        print(Exebition.objects.filter(status_of_exebition = 1).values_list( "type_exebition", flat=True))

        form = RegistrationExhibitionForm()
        return render (request, 'registration_of_dogs/registration_exhibition.html', context = {'form': form})
        
    def post(self, request, **kwards):    
        
        form = RegistrationExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            pass
        

    
