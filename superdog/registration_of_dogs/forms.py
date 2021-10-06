from django.utils.translation import gettext_lazy as _
from django import forms
from .models import RegistrationExhibition, Exebition, AdditionalCategories, Dog, Owner  


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

    def choices_additional_categories():
        """возвращает данные о категориях выставки"""
        class_of_exebition = RegistrationExhibition.objects.all().values('class_of_exebition')
        print(class_of_exebition)


    """1. Поле выставки. Изпользует функцию для отображения названия, даты и места в одном поле формы"""
    exebition = forms.ChoiceField(label=_("Выставка"),choices=choices_open_exebition())
    
    """1. Может использоваться для отображения поля Выставки. Сейчас показывает только ее название"""
    # exebition = forms.ChoiceField(label=_("Выставка"),choices=Exebition.objects.filter(
    #     status_of_exebition = 1).values_list( "date_of_exebition", "type_exebition"))

    """Поле даты рождения собаки. Использует простой виджет"""
    date_of_birth = forms.DateField(label=_("Дата рождения"), widget= forms.SelectDateWidget())

    # эксперимент/ вместо функции choices_additional_categories() и вызова ее в поле. 
    # Работает аналогично, но пока не форматирует правильно данные
    # additional_categories = forms.MultipleChoiceField(label=_("Дополнительные категории"),choices=choices_additional_categories())
    additional_categories = forms.ModelMultipleChoiceField(queryset=Exebition.objects.filter(status_of_exebition = 1).values_list("add_classes_of_exebition__category", flat=True),to_field_name="type_exebition", label=_("Дополнительные категории"))
    # .exclude("None")
    
    class_of_exebition = forms.ChoiceField(label=_("Класс выставки"), choices=RegistrationExhibition.CATEGORY)


    class Meta:
        model = RegistrationExhibition
        fields = (
            # 'class_of_exebition',
            'proof_of_peyment_scanned',
            )
        # model = Dog
        # fields = (
        #     'breed_race',
        #     'gender',
        #     'name_of_dog',
        #     'tattoo_number_microchip',
        #     'studbook_and_registration',
        #     'father_of_dog',
        #     'mother_of_dog',
        #     'breeder_name',
        #     'pedigree_of_dog_scanned_front',
        #     'pedigree_of_dog_scanned_back',
        #     'champion_certificate_scanned',
        #     )
        # model = Owner
        # fields = (
        #     'owner_name',
        #     'owner_telephone',
        #     'owner_email',
        #     )


