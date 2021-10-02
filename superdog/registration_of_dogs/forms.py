# from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebition

class RegistrationExhibitionForm(forms.ModelForm):
    
        
    def choices_open_exebition():
        """функция запрашивает данные об открытых для регистрации 
        выставках и формирует список вариантов"""
        data_of_exebition = Exebition.objects.filter(status_of_exebition = 1)
        # print(Exebition.AdditionalCategories.all())
        open_exebition = []
        for i in data_of_exebition:
            open_exebition.append((str(i.id), "{} - {} - {}".format(i.type_exebition, str(i.date_of_exebition), i.address_exebition))) 
            # print(open_exebition) 
            # print(i.add_classes_of_exebition)
        return open_exebition

    # def multicoices_additional_categories(id_exebition):
    #     """запрашивает данные о доступных дополнительных
    #      категориях открытых выставок"""

    #     exebition = Exebition.objects.filter(id=id_exebition)
    #     return exebition.add_classes_of_exebition

    def choices_additional_categories():
        """данные о всех дополнительных категориях для открытых выставок"""
        data_of_exebition_add = Exebition.objects.filter(status_of_exebition = 1) #открытые выставки
        data_of_exebition = data_of_exebition_add.filter(add_classes_of_exebition=True)#открытые выставки с дополнительными категориями
        additional_categories = []

        print("--"+str(data_of_exebition))
        for i in data_of_exebition:
            print("______________")
            print(i.add_classes_of_exebition )
            # if str(i.add_classes_of_exebition).endswith(None):
            if str(i.add_classes_of_exebition).endswith("None"):
            
                pass
            else:
                additional_categories.append((str(i.id), str(i.add_classes_of_exebition)))  
        return additional_categories



    exebition = forms.ChoiceField(label=_("Выставка"),choices=choices_open_exebition())
    additional_categories = forms.MultipleChoiceField(label=_("Дополнительные категории"),choices=choices_additional_categories())


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