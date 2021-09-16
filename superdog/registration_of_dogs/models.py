from django.db import models
from django.db.models.base import Model

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)

# b1 = AboutUs(titel = "Amber dog", content = "Welcom:)")

class RegistrationExhibition(models.Model):
    '''данные с сайта с формой регистрации'''
    # TYPE OF EXHIBITION
    # EXHIBITION VENUE
    # BREED / RACE
    # THE NAME OF THE DOG
    # TATTOO NUMBER / MICROCHIP
    # STUDBOOK AND REGISTRATION NUMBE
    # DATE OF BIRTH
    # THE FATHER OF THE DOG
    # MOTHER DOG
    # BREEDER'S NAME
    # BREEDER'S ADDRESS
    # NAME OF OWNER
    # OWNER ADDRESS
    # GENDER
    # THE CLASS
    #     YOUNGER PUPPY 3-6 months up to 35cm
    #     YOUNGER PUPPY 3-6 months over 35cm
    #     PUPPY 6-9 months to 35cm
    #     PUPPY 6-9 months over 35cm
    #     YOUNG 9-15 months up to 35cm
    #     YOUNG 9-18 months over 35cm
    #     MEDIUM 15-24 months up to 35cm
    #     MEDIUM 15-24 months over 35cm
    #     OPEN from 15 months to 35cm
    #     OPEN from 18 months over 35cm
    #     CHAMPIONS over 18 months up to 35cm - CERTIFICATE
    #     CHAMPIONS over 18 months over 35cm - CERTIFICATE
    #     VETERANS from 7 years of age up to 35cm
    #     VETERANS from 6 years of age over 35 cm
    #     WORKING from 12 months - Certificate of examination
    #     Final competitions - The most beautiful PAIR of DOGS
    #     Final competitions - The most beautiful BREEDING GROUP
    #     Final competitions - CHILD AND DOG
    # SCANNED (PHOTOGRAPHED) PEDIGREE OF THE DOG - FRONT SIDE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)

    # SCANNED (PHOTOGRAPHED) PEDIGREE OF THE DOG - BACK SIDE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)

    # SCANNED (PHOTOGRAPHED) CHAMPION CERTIFICATE
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)

    # SCANNED (PHOTOGRAPHED) PROOF OF PAYMENT
    # (file in JPG, PNG, or PDF format - max. Size is 6MB)

    # Contact e-mail
    # I confirm that I have become acquainted with the processing of personal data in OZKnS and I hereby give my consent.
    # I agree with the processing of personal data under the GDPR Act.
    # Confirm
    pass

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
    
