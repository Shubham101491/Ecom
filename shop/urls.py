from django.urls import path
from . import views
from .views import watch

# app_name = 'shop'

urlpatterns = [
    # path('watch/',watch.as_view(),name='watch'),
    path('new/<int:id>',views.new,name='new'),
    path('product_detail/<int:id>',views.product_detail,name='product_detail'),
    path('watch/',views.watch,name='watch'),
]