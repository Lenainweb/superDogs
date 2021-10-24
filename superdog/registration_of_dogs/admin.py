from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import AboutUs, Exebition, AdditionalCategories, Owner, Dog, RegistrationExhibition, Fees 

# admin.site.register(AboutUs)
# admin.site.register(Exebition)
admin.site.register(AdditionalCategories)
admin.site.register(Owner)
admin.site.register(Dog)
admin.site.register(RegistrationExhibition)
admin.site.register(Fees)



class AboutUsAdmin(ModelAdmin):
    list_display = ('title', 'published', 'content', 'contacts')


class ExebitionAdmin(ModelAdmin):
    list_display = ('type_exebition', 'date_of_exebition', 'status_of_exebition', 'display_classes_of_exebition')

    

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Exebition, ExebitionAdmin)

