from datetime import date
from django.core import validators
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebition, AdditionalCategories, Dog, Owner  

from phonenumber_field.formfields import PhoneNumberField


class RegistrationExhibitionForm(forms.ModelForm):
    """
    Форма регистрации на выставку
    """
     
    def choices_open_exebition():
        """
        функция запрашивает данные об открытых для регистрации 
        выставках и формирует список вариантов
        """
        data_of_exebition = Exebition.objects.filter(status_of_exebition=True)
        open_exebition = []
        for i in data_of_exebition:                
            open_exebition.append((i.id, "{} - {} - {}".format(
                i.type_exebition, str(i.date_of_exebition.strftime('%d-%m-%Y %H:%M')), i.address_exebition))) 
        return open_exebition

    def choices_additional_categories():
        """
        запрашивает данные о доступных дополнительных
        категориях открытых выставок
        """
        data_of_exebition_add = Exebition.objects.filter(
            status_of_exebition = 1) #открытые выставки
        data_of_exebition = data_of_exebition_add.filter(
            add_classes_of_exebition=True)#открытые выставки с дополнительными категориями
        additional_categories = []

        for i in data_of_exebition:
            data = i.add_classes_of_exebition.all()
            for j in data:
                additional_categories.append((j.id, "{} : - {}".format(
                    i.type_exebition, j.category)))
        print(additional_categories)
        return additional_categories


    """1. Поле выставки. Изпользует функцию для отображения названия, даты и места в одном поле формы"""
    exebition = forms.ChoiceField(label=_("Выставка"),choices=choices_open_exebition(), error_messages={'required': _("Выставка")})
    
    """1. Может использоваться для отображения поля Выставки. Сейчас показывает только ее название"""
    # exebition = forms.ChoiceField(label=_("Выставка"),choices=Exebition.objects.filter(
    #     status_of_exebition = 1).values_list( "date_of_exebition", "type_exebition"))

    

    """3 Поле множественного выбора. Отображает действительные дополнительные категории открытых выставок"""
    # additional_categories = forms.MultipleChoiceField(
    #   label=_("Дополнительные категории"),choices=choices_additional_categories())
#  Работает, но значение не валидируется   
    # additional_categories = forms.ModelMultipleChoiceField(
    #     queryset=Exebition.objects.filter(
    #         status_of_exebition = 1).exclude(
    #             add_classes_of_exebition__category=None).values_list(
    #                 "add_classes_of_exebition__id", "add_classes_of_exebition__category"),
    #         to_field_name="type_exebition", label=_("Дополнительные категории"), required=False) 
    
    # additional_categories = forms.ModelMultipleChoiceField(
    #     queryset=Exebition.objects.filter(
    #         status_of_exebition = 1).exclude(
    #             add_classes_of_exebition__category=None).values(
    #                 "add_classes_of_exebition__id").values("add_classes_of_exebition__category"),
    #         to_field_name="type_exebition", label=_("Дополнительные категории"), required=False)

    '''если вставить после фильтр, создаст список для каждой категории айди-название: 
    .values_list("add_classes_of_exebition__id", "add_classes_of_exebition__category")'''
       
    
    """2. Поле выбора основной категории выставки"""
    # class_of_exebition = forms.ChoiceField(label=_("Класс выставки"), choices=RegistrationExhibition.CATEGORY)
    
    class Meta:
        model = RegistrationExhibition
        fields = (
            'class_of_exebition',
            'additional_classes',
            'proof_of_peyment_scanned',)

       
class DogRegistrationExhibitionForm(forms.ModelForm):
    """
    Форма регистрации собаки 
    """

    """Поле даты рождения собаки. Использует простой виджет"""
    date_of_birth = forms.DateField(label=_("Дата рождения"), 
        widget= forms.SelectDateWidget(years=range(date.today().year, date.today().year - 20, -1)))

    class Meta:
        model = Dog
        fields = (
            'breed_race',
            'gender',
            'name_of_dog',
            'tattoo_number_microchip',
            'studbook_and_registration',
            'father_of_dog',
            'mother_of_dog',
            'breeder_name',
            'pedigree_of_dog_scanned_front',
            'pedigree_of_dog_scanned_back',
            'champion_certificate_scanned',
            ) 

class OwnerRegistrationExhibitionForm(forms.ModelForm):
    """
    Форма регистрации хозяина
    """
    class Meta:
        model = Owner
        fields = (
            'owner_name',
            'owner_telephone',
            'owner_email',
            )

