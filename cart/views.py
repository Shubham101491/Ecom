from django.shortcuts import render,redirect
from ecom import settings

from cart.models import Products
from cart.forms import ProductsForm

# Authnticate APIs
def carts(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('http://127.0.0.1:8000/cart/show/')
            except:
                pass
    else:
        form = ProductsForm()
        return render(request,'cart/cart.html',{"BASE_URL":settings.BASE_URL,'form':form}) 
        
def show(request):
    a = Products.objects.all()
    return render(request,'cart/show.html',{"BASE_URL":settings.BASE_URL,'shop':a})

def edit(request,id):
    b = Products.objects.get(id=id)
    return render(request,'cart/edit.html',{"BASE_URL":settings.BASE_URL,'order':b})

def update(request,id):
    c = Products.objects.get(id=id)
    form = ProductsForm(request.POST,instance= c)

    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/cart/show/")

    return render(request,'cart/edit.html',{"BASE_URL":settings.BASE_URL,'order':c})

def delete(request,id):
    d = Products.objects.get(id=id)
    d.delete()
    return redirect('http://127.0.0.1:8000/cart/show/')