from django import forms
from .models import RegistrationExhibition, AgreePersonalData

class RegistrationExhibitionForm(forms.ModelForm):
    class Meta:
        model = RegistrationExhibition
        fields = ('type_of_exebition', 
            'exebition_venue',
            'breed_race', 
            'name_of_dog', 
            'tattoo_number_microchip',
            'studbook_and_registration', 
            'date_of_birth', 
            'father_of_dog', 
            'mother_of_dog', 
            'breeder_name', 
            'breeder_address',
            'name_of_owner', 
            'owner_address', 
            'gender', 
            'the_class',
            'pedigree_of_dog_scanned_front', 
            'pedigree_of_dog_scanned_back', 
            'champion_certificate_scanned', 
            'proof_of_peyment_scanned', 
            'contact_email')