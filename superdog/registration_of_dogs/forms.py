# from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebition

class RegistrationExhibitionForm(forms.ModelForm):
    
        
    def choices_open_exebition():
        """функция запрашивает данные об открытых для регистрации 
        выставках и формирует список вариантов"""
        data_of_exebition = Exebition.objects.filter(status_of_exebition = 1)
        value = []
        count = 0
        for i in data_of_exebition:
            
            value.append((count, "{} - {} - {}".format(i.type_exebition, str(i.date_of_exebition), i.address_exebition)))  
            count += 1
        print(value)
        return value


    exebition = forms.ChoiceField(label=_("Выставка"),choices=choices_open_exebition())

    class Meta:
        model = Exebition
        fields = ( 
            'add_classes_of_exebition', 
            )
        model = RegistrationExhibition
        fields = (
            'class_of_exebition',
            )

    date_of_birth = forms.DateField(label=_("Дата рождения"), widget= forms.SelectDateWidget())
    """остановилась на запросе данных с базы выставок о связанных дополнительных карегориях""" 