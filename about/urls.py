from django.urls import path
from . import views

urlpatterns = [
    path('about_shop/',views.about_shop,name='about_shop'),
]