from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from django.contrib import messages

from .models import AboutUs, RegistrationExhibition, Exebition, AdditionalCategories, Dog, Owner
from .forms import RegistrationExhibitionForm, DogRegistrationExhibitionForm, OwnerRegistrationExhibitionForm

class HomePageView(TemplateView):
    """Главная страница
    отображает контент из таблицы О НАС"""
    
    def get(self, request, **kwargs):
        date = AboutUs.objects.last()
        
        test = request.LANGUAGE_CODE
        return render(request, 'registration_of_dogs/index.html', 
            context = {'title' : date.title, 'content': _(date.content), 'test': test})


class RegistrationExhibitionView(TemplateView):
    """Страница регистрации на выставку"""
    
    def get(self, request, **kwargs):
        """Отрисовует форму регистрации на выставку"""
        form_registr = RegistrationExhibitionForm()
        form_dog = DogRegistrationExhibitionForm()
        form_owner = OwnerRegistrationExhibitionForm()
        return render (request, 'registration_of_dogs/registration_exhibition.html', 
            context = {'form_registr': form_registr, 
                'form_dog': form_dog, 
                'form_owner': form_owner })
        
    def post(self, request, **kwards):
        """Обрабатывает и сохраняет данные из формы регистрации""" 
        # получение данных из форм   
        form_registr = RegistrationExhibitionForm(request.POST, request.FILES)
        form_dog = DogRegistrationExhibitionForm(request.POST, request.FILES)
        form_owner = OwnerRegistrationExhibitionForm(request.POST)
        
        # валидация форм и сохранение
        if form_owner.is_valid() and form_registr.is_valid() and form_dog.is_valid():
            # заполнение таблицы ХОЗЯИН
            owner = form_owner.save(commit=False)
            owner.save()
            # заполнение таблицы СОБАКА
            dog = form_dog.save(commit=False)
            dog.date_of_birth = form_dog.cleaned_data["date_of_birth"]
            dog.name_of_owner = owner
            dog.save()
            # заполнение таблицы РЕГИСТРАЦИЯ
            register = form_registr.save(commit=False)
            register.exebition = Exebition.objects.get(id=int(form_registr.cleaned_data["exebition"]))
            register.dog = dog
            register.owner = owner
            register.class_of_exebition = form_registr.cleaned_data["class_of_exebition"]
            register.save()
            # создание связи записи регистрации с выбранными дополнительными категориями
            register.additional_classes.set(form_registr.cleaned_data["additional_classes"])
            # сообщение о успешной регистрации
            messages.success(request, 'Your forms successfully!')
        else:
            # сообщение с указанием ошибок при заполнении формы
            messages.error(request, form_owner.errors, form_registr.errors, form_dog.errors)

        return redirect('/')
        
