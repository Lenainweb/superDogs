from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import AboutUs, Exebition, AdditionalCategories, Owner, Dog, RegistrationExhibition, Fees 

# admin.site.register(AboutUs)
# admin.site.register(Exebition)
# admin.site.register(AdditionalCategories)
# admin.site.register(Owner)
# admin.site.register(Dog)
# admin.site.register(RegistrationExhibition)
# admin.site.register(Fees)



class AboutUsAdmin(ModelAdmin):
    list_display = ('title', 'published', 'content', 'contacts')


class ExebitionAdmin(ModelAdmin):
    list_display = ('type_exebition', 'date_of_exebition', 'status_of_exebition', 'display_classes_of_exebition')

class AdditionalCategoriesAdmin(ModelAdmin):
    list_display = ('category', 'discreption')


class OwnerAdmin(ModelAdmin):
    list_display = ('owner_name', 'owner_telephone', 'owner_email', 'display_dogs', 'status_of_user')

class DogAdmin(ModelAdmin):
    list_display = ('breed_race', 'name_of_owner', 'name_of_dog', 'date_of_birth')

class RegistrationExhibitionAdmin(ModelAdmin):
    list_display = ('exebition', 'dog', 'class_of_exebition')

class FeesAdmin(ModelAdmin):
    list_display = ('position', 'price')

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Exebition, ExebitionAdmin)
admin.site.register(AdditionalCategories, AdditionalCategoriesAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(RegistrationExhibition, RegistrationExhibitionAdmin)
admin.site.register(Fees, FeesAdmin )





