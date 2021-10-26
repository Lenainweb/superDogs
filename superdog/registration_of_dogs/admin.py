from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.db.models import fields
from .models import AboutUs, Exebition, AdditionalCategories, Owner, Dog, RegistrationExhibition, Fees 


@admin.register(AboutUs) 
class AboutUsAdmin(ModelAdmin):
    list_display = ('title', 'published', 'content', 'contacts')
    save_as = True


class ParticipantInline(admin.TabularInline):
    model = RegistrationExhibition
    extra = 0
    fields = ('dog', 'owner', 'proof_of_peyment_scanned', 'proof_of_payment')
    readonly_fields = ('dog', 'owner', 'proof_of_peyment_scanned',)
    


@admin.register(Exebition)
class ExebitionAdmin(ModelAdmin):
    list_display = ('type_exebition', 'date_of_exebition', 'status_of_exebition', 'display_classes_of_exebition')
    list_filter = ('status_of_exebition',)
    list_editable = ('status_of_exebition',)
    fields = ('type_exebition', 'date_of_exebition', 'add_classes_of_exebition', 'status_of_exebition',)
    inlines = [ParticipantInline]
    # filter_horizontal = ('add_classes_of_exebition',)
    filter_vertical = ('add_classes_of_exebition',)



@admin.register(AdditionalCategories)
class AdditionalCategoriesAdmin(ModelAdmin):
    list_display = ('category', 'discreption')

@admin.register(Owner)
class OwnerAdmin(ModelAdmin):
    list_display = ('owner_name', 'owner_telephone', 'owner_email', 'display_dogs', 'status_of_user')
    list_filter = ('status_of_user',)
    # search_fields = ('owner_name',)
    readonly_fields = ('owner_name', 'owner_telephone', 'owner_email', 'display_dogs', 'status_of_user')


@admin.register(Dog)
class DogAdmin(ModelAdmin):
    list_display = ('name_of_dog', 'breed_race', 'name_of_owner', 'date_of_birth')
    # readonly_fields = ('name_of_dog', 'breed_race', 'name_of_owner', 'date_of_birth')
    list_filter = ('breed_race',)


@admin.register(RegistrationExhibition)
class RegistrationExhibitionAdmin(ModelAdmin):
    list_display = ('exebition', 'dog', 'class_of_exebition', 'date_registration', 'proof_of_payment')
    list_filter = ('exebition', 'class_of_exebition')
    # radio_fields = {'class_of_exebition': admin.VERTICAL}

    

@admin.register(Fees)
class FeesAdmin(ModelAdmin):
    list_display = ('position', 'price')
    # save_on_top = True


