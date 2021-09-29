from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.base import Model

from phonenumber_field.modelfields import PhoneNumberField

class AboutUs(models.Model):
    """Информация отображаемая на главной странице"""
    title = models.CharField(_("Приветствие"), max_length=50)
    content = models.TextField(_("Описание"))
    published = models.DateTimeField(_("Дата публикации"), auto_now_add=True, db_index=True)
    contacts = models.TextField(_("Контакты"))

    def __str__(self):
        return "{0} {1}".format(self.title, self.content)

class Exebition(models.Model):
    """Выставки"""
    class StatusOfExebition(models.IntegerChoices):
        """Открытые для регистрации или уже закрытые выставки"""
        CLOSE = 0, "Close"
        OPEN = 1, "Open"
        
    type_exebition = models.TextField(_("Тип выставки"), max_length=160)
    date_of_exebition = models.DateTimeField(_("Дата и время проведения"))
    address_exebition = models.TextField(_("Место проведения"))
    add_classes_of_exebition = models.ManyToManyField('AdditionalCategories', verbose_name = _("Дополнительные категории" ), blank=True)# THE ADD CLASS
    status_of_exebition = models.IntegerField(_("Статус выставки"), 
        choices=StatusOfExebition.choices, default=StatusOfExebition.OPEN)
    participant_of_exebition = models.ManyToManyField("Dog", verbose_name = _("Участники выставки" ), blank=True)

    def __str__(self):
        return "{0} {1}".format(self.type_exebition, self.date_of_exebition)

class AdditionalCategories(models.Model):
    """Дополнительные категории выставки"""
        # WORKING = '15', _("WORKING from 12 months - Certificate of examination")
        # PAIR_DOGS = '16', _("Final competitions - The most beautiful PAIR of DOGS")
        # BREEDING_GROUP = '17', _("Final competitions - The most beautiful BREEDING GROUP")
        # CHILD_AND_DOG = '18', _("Final competitions - CHILD AND DOG")
    category = models.TextField(_("Название категории"),max_length=50)
    discreption =  models.TextField(_("Описание"),max_length=50)

    

    def __str__(self):
            return self.category

class Owner(models.Model):
    """Владелец"""
    owner_name = models.TextField(_("Имя владельца"), max_length=50)
    owner_telephone = PhoneNumberField(_("Телефон владельца"), blank=True)
    owner_email = models.EmailField(_("Почта владельца"))
    status_of_user = models.BooleanField(_("Статус (зарегестрирован/без регистрации"),default=False)

    def __str__(self):
        return self.owner_name


class Dog(models.Model):
    """Собака"""
    class GenderDog(models.IntegerChoices):
        """Пол собаки"""
        MALE = 0, "Male"
        FEMALE = 1, "Female"

    breed_race = models.CharField(_("Порода"), max_length=50)# BREED / RACE
    gender = models.IntegerField(_("Пол"), choices=GenderDog.choices, default=GenderDog.MALE)# GENDER
    name_of_dog = models.CharField(_("Кличка"), max_length=50)# THE NAME OF THE DOG
    tattoo_number_microchip = models.CharField(_("Номер чипа"), max_length=50)# TATTOO NUMBER / MICROCHIP
    studbook_and_registration = models.CharField(_("Номер регистрации"), max_length=50)# STUDBOOK AND REGISTRATION NUMBE
    date_of_birth = models.DateField(_("Дата рождения"))# DATE OF BIRTH
    father_of_dog = models.CharField(_("Отец"), max_length=50)# THE FATHER OF THE DOG
    mother_of_dog = models.CharField(_("Мать"), max_length=50)# MOTHER DOG
    breeder_name = models.CharField(_("Имя заводчика"), max_length=50)# BREEDER'S NAME
    name_of_owner = models.ForeignKey('Owner', help_text="Имя владельца", related_name="name_of_owner", on_delete=models.PROTECT)

    # SCANNED (PHOTOGRAPHED) PEDIGREE OF THE DOG - FRONT SIDE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    pedigree_of_dog_scanned_front = models.ImageField("Паспорт фронт",upload_to="files/download/pedigree_of_dog")
    
    # SCANNED (PHOTOGRAPHED) PEDIGREE OF THE DOG - BACK SIDE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    pedigree_of_dog_scanned_back = models.ImageField("Паспорт тыл", upload_to="files/download/pedigree_of_dog")

    # SCANNED (PHOTOGRAPHED) CHAMPION CERTIFICATE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    champion_certificate_scanned = models.ImageField("Сертификат чемпиона", upload_to="files/download/champion_certificate",  blank=True)

    # SCANNED (PHOTOGRAPHED) PROOF OF PAYMENT
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    proof_of_peyment_scanned = models.ImageField("Оплата сбора",upload_to="files/download/proof_of_peyment")

    
    def __str__(self):
        return "Собака: {0}, хозяин:{1}".format(self.name_of_dog, self.name_of_owner)



class RegistrationExhibition(models.Model):
    """Регистрация собаки на выставке"""
    class ClassOfEexebition(models.TextChoices):
        """Категории"""
        YOUNGER_PUPPY_UP = '1', _("YOUNGER PUPPY 3-6 months up to 35cm")
        YOUNGER_PUPPY_OV = '2', _("YOUNGER PUPPY 3-6 months over 35cm")
        PUPPY_UP = '3', _("PUPPY 6-9 months to 35cm")
        PUPPY_OV = '4', _("PUPPY 6-9 months over 35cm")
        YOUNG_YO = '5', _("YOUNG 9-15 months up to 35cm")
        YOUNG_OV = '6', _("YOUNG 9-18 months over 35cm")
        MEDIUM_TO = '7', _("MEDIUM 15-24 months up to 35cm")
        MEDIUM_OV = '8', _("MEDIUM 15-24 months over 35cm")
        OPEN_TO = '9', _("OPEN from 15 months to 35cm")
        OPEN_OV = '10', _("OPEN from 18 months over 35cm")
        CHAMPIONS_TO = '11', _("CHAMPIONS over 18 months up to 35cm - CERTIFICATE")
        CHAMPIONS_OV = '12', _("CHAMPIONS over 18 months over 35cm - CERTIFICATE")
        VETERANS_TO = '13', _("VETERANS from 7 years of age up to 35cm")
        VETERANS_OV = '14', _("VETERANS from 6 years of age over 35 cm")
        WORKING = '15', _("WORKING from 12 months - Certificate of examination")
        PAIR_DOGS = '16', _("Final competitions - The most beautiful PAIR of DOGS")
        BREEDING_GROUP = '17', _("Final competitions - The most beautiful BREEDING GROUP")
        CHILD_AND_DOG = '18', _("Final competitions - CHILD AND DOG")

    exebition= models.ForeignKey(Exebition, verbose_name=_("Выставка"), related_name="exebition", on_delete=models.PROTECT)
    dog = models.ForeignKey('Dog', verbose_name=_("Кличка") , related_name="dog", on_delete=models.PROTECT)# THE NAME OF THE DOG
    owner = models.ForeignKey('Owner', verbose_name=_("Имя хозяина"), related_name="owner", on_delete=models.PROTECT)# NAME OF OWNER
    class_of_exebition = models.TextField("Категория", choices=ClassOfEexebition.choices)# THE CLASS
    additional_classes = models.ManyToManyField('AdditionalCategories', verbose_name=_("Дополнительные котегории"), blank=True)
    

class Fees(models.Model):
    position = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.position

    
