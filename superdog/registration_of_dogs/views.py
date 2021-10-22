from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from django.contrib import messages

from .models import AboutUs, RegistrationExhibition, Exebition, AdditionalCategories, Dog, Owner
from .forms import RegistrationExhibitionForm, DogRegistrationExhibitionForm, OwnerRegistrationExhibitionForm

class HomePageView(TemplateView):
    
    def get(self, request, **kwargs):
        date = AboutUs.objects.last()
        
        test = request.LANGUAGE_CODE
        return render(request, 'registration_of_dogs/index.html', 
            context = {'title' : date.title, 'content': _(date.content), 'test': test})


class RegistrationExhibitionView(TemplateView):
    
    def get(self, request, **kwargs):
        form_registr = RegistrationExhibitionForm()
        form_dog = DogRegistrationExhibitionForm()
        form_owner = OwnerRegistrationExhibitionForm()
        return render (request, 'registration_of_dogs/registration_exhibition.html', 
            context = {'form_registr': form_registr, 'form_dog': form_dog, 'form_owner': form_owner })
        
    def post(self, request, **kwards):    
        # form = RegistrationExhibitionForm(request.POST)
        form_registr = RegistrationExhibitionForm(request.POST, request.FILES)
        form_dog = DogRegistrationExhibitionForm(request.POST, request.FILES)
        form_owner = OwnerRegistrationExhibitionForm(request.POST)
        
        if form_registr.is_valid():
            # cleaned_data
            # form.save()
            print("form_registr:")
            print(form_registr.cleaned_data)
            messages.info(request, 'Your form_registr successfully!')

        else:
            print("form_registr: errors:")
            print(form_registr.errors)
        
        if form_dog.is_valid():
            # cleaned_data
            # form.save()
            print("form_dog:")
            print(form_dog.cleaned_data)
        else:
            print("form_dog: errors:")
            print(form_dog.errors)

        if form_owner.is_valid():
            # cleaned_data
            # form.save()
            print("form_owner:")
            print(form_owner.cleaned_data)
        else:
            print("form_owner: errors:")
            print(form_owner.errors) 

        # else:

        #     print("-------------------------")
        #     print(form.errors)
            # messages.success(request, f'ygy!')
        return redirect('/')
        
"""-------------------------
<QueryDict: {'csrfmiddlewaretoken': ['goUbIZzBjLBNnpXL6WEXqs6LBKKmgs2ErtyRjKQnXGFFP07Hv4fwYOFer5MMLCQO'],
 'exebition': ['6'], 'class_of_exebition': ['YOUNGER_PUPPY_UP'], 'additional_categories': ['Дополнительная категория'],
  'breed_race': ['Единорог'], 'gender': ['0'], 'name_of_dog': ['asd'], 'tattoo_number_microchip': ['666'], 
  'studbook_and_registration': ['dghd'], 'date_of_birth_day': ['1'], 'date_of_birth_month': ['1'], 
  'date_of_birth_year': ['2021'], 'father_of_dog': ['конь'], 'mother_of_dog': ['носорог'], 
  'breeder_name': ['Эксперт'], 'owner_name': ['hghnjjj'], 'owner_telephone': ['sssssssssss'], 
  'owner_email': ['sdddd@dfg.fg'], 'pedigree_of_dog_scanned_front': ['ajax-loader.gif'], 
  'pedigree_of_dog_scanned_back': ['en.png'], 'champion_certificate_scanned': [''], 
  'proof_of_peyment_scanned': ['pl.png']}>"""
    
'''<ul class="errorlist"><
li>pedigree_of_dog_scanned_front<ul class="errorlist"><li>Обязательное поле.</li></ul>
</li><li>pedigree_of_dog_scanned_back<ul class="errorlist"><li>Обязательное поле.</li></ul><
/li><li>additional_categories<ul class="errorlist"><li>Выберите корректный вариант. 
Дополнительная категория нет среди допустимых значений.</li></ul>
</li><li>proof_of_peyment_scanned<ul class="errorlist"><li>Обязательное поле.</li></ul><
/li><li>owner_name<ul class="errorlist"><li>Выберите корректный вариант. Я нет среди допустимых значений.</li></ul>
</li><li>owner_telephone<ul class="errorlist"><li>Введите корректный номер телефона (например, +12125552368).</li></ul><
/li></ul>'''