from django.urls import path

from .views import index, registration_exhibition

urlpatterns = [
    path('', index),
    path('registration_exhibition/', registration_exhibition),

]