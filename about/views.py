from django.shortcuts import render
from ecom import settings

def about_shop(request):
    return render(request,'about/about.html',{"BASE_URL":settings.BASE_URL})
