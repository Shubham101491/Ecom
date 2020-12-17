from django.urls import path
from . import views

urlpatterns = [
    path('carts/',views.carts,name='carts'),
    path('show/',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]