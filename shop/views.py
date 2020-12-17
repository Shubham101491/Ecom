from django.shortcuts import render,redirect
from ecom import settings

from shop.models import Watch,Category
from django.views import View

# Example of CBV (post and Get both using same function)
# Class Base View
# class watch(View):
#     def post(self, request):
#         prod = request.POST.get('product')
#         # print(prod)
#         cart = request.session.get('cart')
#         if cart:
#             quantity = cart.get(prod)
#             if quantity:
#                 cart[prod] = quantity+1
#             else:
#                 cart[prod] = 1
#         else:
#             cart = {}
#             cart[prod] = 1
#         request.session['cart'] = cart
#         print('cart' ,request.session['cart'])
#         return redirect('/shop/pag')

#     def get(self, request):
#         shp = None
#         # request.session.get('cart').clear()
#         catego = Category.objects.all()
#         categoryID = request.GET.get('category')

#         if categoryID:
#             shp = Watch.objects.filter(category_id = categoryID)
#         else:
#             shp = Watch.objects.all()
#         data = {}
#         data['shop'] = shp
#         data['categ'] = catego
#         data['BASE_URL'] = settings.BASE_URL
#         print('you are : ', request.session.get('email'))
#         return render(request,'shop/watch.html',data)

# Authnticate APIs
def new(request,id):
    prod = request.POST.get('product')
    remove = request.POST.get('remove')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(prod)
        if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(prod)
                else:
                    cart[prod] = quantity-1
            else:
                cart[prod] = quantity+1
        else:
            cart[prod] = 1
    else:
        cart = {}
        cart[prod] = 1
    request.session['cart'] = cart
    print('cart' ,request.session['cart'])
    # show add product in list
    ids = list(request.session.get('cart').keys())
    allimages = Watch.objects.filter(id__in=ids)
    return render(request,'pages/cart.html',{"BASE_URL":settings.BASE_URL,'images':allimages})

def watch(request):
    shp = None
    catego = Category.objects.all()
    categoryID = request.GET.get('category')

    if categoryID:
        shp = Watch.objects.filter(category_id = categoryID)
    else:
        shp = Watch.objects.all()
    data = {}
    data['shop'] = shp
    data['categ'] = catego
    data['BASE_URL'] = settings.BASE_URL
    print('you are : ', request.session.get('email'))
    return render(request,'shop/watch.html',data)

# For Product detail
def product_detail(request,id):
    allimages = Watch.objects.filter(id=id)
    return render(request,'letest/product_details.html',{"BASE_URL":settings.BASE_URL,'images':allimages})