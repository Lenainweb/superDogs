from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('registration_exhibition/', RegistrationExhibitionView.as_view(), name='registration'),
    path('shows_list/', ShowsList.as_view(), name='shows'),
    path('show-<slug:slug>/', ShowDetail.as_view(), name='show_detail'),
]