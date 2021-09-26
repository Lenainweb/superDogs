from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.base import Model

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)

# b1 = AboutUs(titel = "Amber dog", content = "Welcom:)")

class Exhibitions(models.Model):

    class AddClassesOfEexebition(models.TextChoices):
        WORKING = '15', _("WORKING from 12 months - Certificate of examination")
        PAIR_DOGS = '16', _("Final competitions - The most beautiful PAIR of DOGS")
        BREEDING_GROUP = '17', _("Final competitions - The most beautiful BREEDING GROUP")
        CHILD_AND_DOG = '18', _("Final competitions - CHILD AND DOG")

    class StatusOfExebition(models.IntegerChoices):
        CLOSE = 0, "Close"
        OPEN = 1, "Open"
        
    type_of_exebition = models.CharField(_("Тип выставки"), help_text= _("Тип выставки"), max_length=160)# TYPE OF EXHIBITION
    date_of_exebition = models.DateTimeField()
    address_of_exebition = models.TextField()
    add_classes_of_exebition = models.TextField(_("Дополнительные категории"), choices=AddClassesOfEexebition.choices)# THE ADD CLASS
    status_of_exebition = models.IntegerField(_("Статус выставки"), choices=StatusOfExebition.choices, default=StatusOfExebition.OPEN)


class RegistrationExhibition(models.Model):

    class GenderDog(models.IntegerChoices):
        MALE = 0, "Male"
        FEMALE = 1, "Female"

    class ClassOfEexebition(models.TextChoices):
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



    '''данные с сайта с формой регистрации'''
    
    exebition_venue = models.CharField("Место проведения", max_length=160)# EXHIBITION VENUE
    breed_race = models.CharField("Порода", max_length=50)# BREED / RACE
    name_of_dog = models.CharField("Кличка", max_length=50)# THE NAME OF THE DOG
    tattoo_number_microchip = models.CharField("Номер чипа", max_length=50)# TATTOO NUMBER / MICROCHIP
    studbook_and_registration = models.CharField("Номер регистрации", max_length=50)# STUDBOOK AND REGISTRATION NUMBE
    date_of_birth = models.DateTimeField("Дата рождения", )# DATE OF BIRTH
    father_of_dog = models.CharField("Отец", max_length=50)# THE FATHER OF THE DOG
    mother_of_dog = models.CharField("мать", max_length=50)# MOTHER DOG
    breeder_name = models.CharField("Имя заводчика", max_length=50)# BREEDER'S NAME
    breeder_address = models.CharField("Адрес заводчика", max_length=50)# BREEDER'S ADDRESS
    name_of_owner = models.CharField("Имя хозяина", max_length=50)# NAME OF OWNER
    owner_address = models.CharField("Адрес хозяина", max_length=50)# OWNER ADDRESS
    gender = models.IntegerField("Пол", choices=GenderDog.choices, default=GenderDog.MALE)# GENDER
    class_of_exebition = models.TextField("Категория", choices=ClassOfEexebition.choices)# THE CLASS
    
            
    
    # SCANNED (PHOTOGRAPHED) PEDIGREE OF THE DOG - FRONT SIDE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    pedigree_of_dog_scanned_front = models.FileField("Паспорт фронт", )
    
    # SCANNED (PHOTOGRAPHED) PEDIGREE OF THE DOG - BACK SIDE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    pedigree_of_dog_scanned_back = models.FileField("Паспорт тыл", )

    # SCANNED (PHOTOGRAPHED) CHAMPION CERTIFICATE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    champion_certificate_scanned = models.FileField("Сертификат чемпиона", )

    # SCANNED (PHOTOGRAPHED) PROOF OF PAYMENT
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)
    proof_of_peyment_scanned = models.FileField("Оплата сбора", )

    contact_email = models.EmailField("Email") # Contact e-mail
    # I confirm that I have become acquainted with the processing of personal data in OZKnS and I hereby give my consent.
    # I agree with the processing of personal data under the GDPR Act.
    # Confirm
    

# class AgreePersonalData(models.Model):
#     '''данные с сайта с формой регистрации'''
#     # I confirm that I have become acquainted with the processing of personal data in OZKnS and I hereby give my consent.
#     # I agree with the processing of personal data under the GDPR Act.
#     pass

# class CategoryExebition(models.Model):
#     '''данные с сайта с формой регистрации'''
#     #     YOUNGER PUPPY 3-6 months up to 35cm
#     #     YOUNGER PUPPY 3-6 months over 35cm
#     #     PUPPY 6-9 months to 35cm
#     #     PUPPY 6-9 months over 35cm
#     #     YOUNG 9-15 months up to 35cm
#     #     YOUNG 9-18 months over 35cm
#     #     MEDIUM 15-24 months up to 35cm
#     #     MEDIUM 15-24 months over 35cm
#     #     OPEN from 15 months to 35cm
#     #     OPEN from 18 months over 35cm
#     #     CHAMPIONS over 18 months up to 35cm - CERTIFICATE
#     #     CHAMPIONS over 18 months over 35cm - CERTIFICATE
#     #     VETERANS from 7 years of age up to 35cm
#     #     VETERANS from 6 years of age over 35 cm
#     #     WORKING from 12 months - Certificate of examination
#     #     Final competitions - The most beautiful PAIR of DOGS
#     #     Final competitions - The most beautiful BREEDING GROUP
#     #     Final competitions - CHILD AND DOG
#     pass


class Fees(models.Model):
    position = models.TextField()
    price = models.PositiveIntegerField()
    '''данные с сайта позиции с расценками'''
    # For 1 (adult) dog - 40 €

    # Juniors and veterans - 25 €
    # Younger and older adolescents - 20 €
    # Registration of the dog on the day of the show - 50 € for each dog, regardless of age

    # Additional competitions:

    # The most beautiful pair of dogs - 20 €
    # breeding group - 20 €
    # Child and dog - FREE OF CHARGE!
    # Registration deadline 10 days before the start of the exhibition
    # Fill out a separate application for each dog! Attach a photocopy of the dog's pedigree to the application!
    # Attach a photocopy of the payment of entry fees to the application!
    # Entry to the caravan park is conditioned by a fee of 3, -Euro / person / car
    # Accommodation can be provided through www.atcvarin.sk
    
