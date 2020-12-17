from django.urls import path,include
from . import views
# from .views import Checkout

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    ########################################
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password_change', include('django.contrib.auth.urls')),

    # path('change-password/',views.change_password,name='change_password'),
    
    ###########################################################
    path('checkout/',views.checkout,name='checkout'),
    # Paytm Payment Gateway
    path('handlerequest/',views.handlerequest,name='handlerequest'),
    # path('checkout/',Checkout.as_view(),name='checkout'),
    path('elements/',views.elements,name='elements'),
    path('confirmation/',views.confirmation,name='confirmation'),

]