from django.shortcuts import render, HttpResponse
from ecom import settings


def index(request):
    return render(request, 'home/index.html', {"BASE_URL": settings.BASE_URL})
