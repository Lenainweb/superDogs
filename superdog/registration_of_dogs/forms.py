# from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebitions

class RegistrationExhibitionForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(label=_("Дата рождения"), widget= forms.SelectDateWidget())
    exebition_type = forms.ModelChoiceField(queryset=Exebitions.objects.all(), empty_label=None)
    exebition_venue = forms.ModelChoiceField(queryset=Exebitions.objects.all(), empty_label=None)
    
    
    class Meta:
        model = RegistrationExhibition
        fields = ( 
            'breed_race', 
            'name_of_dog', 
            'tattoo_number_microchip',
            'studbook_and_registration',  
            'father_of_dog', 
            'mother_of_dog', 
            'breeder_name', 
            'breeder_address',
            'name_of_owner', 
            'owner_address', 
            'gender', 
            'class_of_exebition',
            'pedigree_of_dog_scanned_front', 
            'pedigree_of_dog_scanned_back', 
            'champion_certificate_scanned', 
            'proof_of_peyment_scanned', 
            'contact_email')