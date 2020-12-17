from django.contrib import admin
from shop.models import Watch,Category,Order

class AdminWatch(admin.ModelAdmin):
    list_display = ['id','watch_title','category','watch_detail','watch_price']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Watch,AdminWatch)
admin.site.register(Category,AdminCategory)
admin.site.register(Order)