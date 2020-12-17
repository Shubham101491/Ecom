"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# admin header and title name change
admin.site.site_header = "Ecommerce"
admin.site.site_title = "Shop Site"
admin.site.index_title = "Shop and Blog Site"

# Media Part
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('shop/',include('shop.urls')),
    path('about/',include('about.urls')),
    path('letest/',include('letest.urls')),
    path('blog/',include('blog.urls')),
    path('pages/',include('pages.urls')),
    path('contact/',include('contact.urls')),
    path('cart/',include('cart.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)