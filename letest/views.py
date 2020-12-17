from django.shortcuts import render
from ecom import settings
from shop.models import Watch,Category


# Authnticate APIs
def product_list(request):
    shp = Watch.objects.all()
    data = {}
    data['shop'] = shp
    return render(request,'shop/watch.html',data,{"BASE_URL":settings.BASE_URL})

def product_detail(request):
    all = Watch.objects.all()
    return render(request,'letest/product_details.html',{"BASE_URL":settings.BASE_URL,'images':all})