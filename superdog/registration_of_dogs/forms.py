# from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebition

class RegistrationExhibitionForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(label=_("Дата рождения"), widget= forms.SelectDateWidget())
    # exebition_type = forms.ModelChoiceField(queryset=Exebition.objects.all(), empty_label=None)
    # exebition_venue = forms.ModelChoiceField(queryset=Exebition.objects.all(), empty_label=None)
    
    
    class Meta:
        model = RegistrationExhibition
        fields = ( 
            'exebition',
            'dog',
            'owner',
            'class_of_exebition',
            'additional_classes')
    