from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebition, AdditionalCategories, Dog, Owner  

from phonenumber_field.formfields import PhoneNumberField



class RegistrationExhibitionForm(forms.ModelForm):
    """
    Форма регистрации собаки на выставки, работает с данными моделей Зарегестрированных, 
    Выставок, Дополнительных категорий, Собак, Хозяев
    """
     
    def choices_open_exebition():
        """
        функция запрашивает данные об открытых для регистрации 
        выставках и формирует список вариантов
        """
        data_of_exebition = Exebition.objects.filter(status_of_exebition = 1)
        open_exebition = []
        for i in data_of_exebition:                
            open_exebition.append((str(i.id), "{} - {} - {}".format(
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
            # print("______________")
            # print(i.add_classes_of_exebition.all())
            data = i.add_classes_of_exebition.all()
            for j in data:
                # print(j)
                # additional_categories.append((str(j.id), j.category))
                additional_categories.append((str(j.id), "{} : - {}".format(
                    i.type_exebition, j.category)))
        return additional_categories


    """1. Поле выставки. Изпользует функцию для отображения названия, даты и места в одном поле формы"""
    exebition = forms.ChoiceField(label=_("Выставка"),choices=choices_open_exebition())
    
    """1. Может использоваться для отображения поля Выставки. Сейчас показывает только ее название"""
    # exebition = forms.ChoiceField(label=_("Выставка"),choices=Exebition.objects.filter(
    #     status_of_exebition = 1).values_list( "date_of_exebition", "type_exebition"))

    """Поле даты рождения собаки. Использует простой виджет"""
    date_of_birth = forms.DateField(label=_("Дата рождения"), widget= forms.SelectDateWidget())

    """3 Поле множественного выбора. Отображает действительные дополнительные категории открытых выставок"""
    # additional_categories = forms.MultipleChoiceField(label=_("Дополнительные категории"),choices=choices_additional_categories())
    additional_categories = forms.ModelMultipleChoiceField(
        queryset=Exebition.objects.filter(status_of_exebition = 1).values_list(
            "add_classes_of_exebition__category", flat=True).exclude(add_classes_of_exebition__category=None) ,
            to_field_name="type_exebition", label=_("Дополнительные категории"), blank=True)
       
    
    """2. Поле выбора основной категории выставки"""
    class_of_exebition = forms.ChoiceField(label=_("Класс выставки"), choices=RegistrationExhibition.CATEGORY)

    """19. Поле для загрузки фото- или сканкопии чека об оплате сбора"""
    proof_of_peyment_scanned = forms.ImageField(label=_("Чек об оплате сбора"))


    """19. Поле для загрузки фото- или сканкопии чека об оплате сбора"""
    # proof_of_peyment_scanned = forms.ImageField(label=_("Чек об оплате сбора"))


    """"""
    # breed_race = forms.CharField(label=_("Порода"))
    # gender = forms.ChoiceField(label=_("Пол"), choices=Dog.GenderDog.choices)

    """"""
    owner_name = forms.ChoiceField(label=_("Имя владельца"))
    owner_telephone = PhoneNumberField(label=_("Телефон владельца"))
    owner_email = forms.EmailField(label=_("Почта владельца"))




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
        


