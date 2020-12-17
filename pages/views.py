from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from ecom import settings
from pages.forms import UserForm, RegisterForm
from shop.models import Watch, Order
from django.contrib import messages

from django.contrib import auth
from django.views import View

# for User authentication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Paytm payment gateway
from django.views.decorators.csrf import csrf_exempt
# from paytmchecksum import PaytmChecksum
from pages import checksum
MERCHANT_KEY = 'BI&B@DfXxG7OWNBd'


# Authnticate APIs
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        register_form = RegisterForm(data=request.POST)

        if user_form.is_valid() and register_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            regis = register_form.save(commit=False)
            regis.user = user

            regis.save()
            registered = True
        else:
            print(user_form.errors, register_form.errors)

    else:
        user_form = UserForm()
        register_form = RegisterForm()
        # return redirect ('http://127.0.0.1:8000/pages/login/')
    return render(
        request, 'pages/register.html', {
            "BASE_URL": settings.BASE_URL,
            'user_form': user_form,
            'register_form': register_form,
            'registered': registered
        })


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        register_user = auth.authenticate(username=username, password=password)
        if register_user:
            request.session['register_user'] = register_user.id
            request.session['email'] = register_user.email
            messages.info(request, 'Thankyou for Login Here,Feel Free to Shop')
            return redirect('/shop/watch/')
        else:
            messages.info(request, 'Incorrect Username & Password')
            return redirect('/pages/login/')
    else:
        return render(request, 'pages/login.html',
                      {"BASE_URL": settings.BASE_URL})


def logout(request):
    request.session.clear()
    messages.info(request, 'Logout Successfull')
    return redirect('login')


# def change_password(request):
#     form = UserCreationForm()
#     return render(request,'registration/password_change_form.html',{"BASE_URL": settings.BASE_URL,'form':form})


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        customer = request.session.get('register_user')
        cart = request.session.get('cart')
        # list of customer order product with quantity
        ids = list(request.session.get('cart').keys())
        products = Watch.objects.filter(id__in=ids)
        print(address, customer, products, cart)

        for product in products:
            order = Order(
                product=product,
                price=product.watch_price,
                address=address,
            )
        request.session['cart'] = {}
        order.placeOrder()
        # request paytm to trasfer user amount
        param_dict = {
            # Local variable checksum error 37:43 video
            # yYzRdS69774940605473
            'MID': 'qofSIN69628291597131',
            'ORDER_ID': 'order.order_id',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            # Change Callback_URl to your ip
            'CALLBACK_URL': 'http://127.0.0.1:8000/pages/handlerequest/',
        }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(
        param_dict, MERCHANT_KEY)
    return render(request, 'pages/paytm.html', {'param_dict': param_dict})

    # messages.info(request, 'Order Successful')
    # return render(request,'pages/cart.html',{"BASE_URL":settings.BASE_URL})


@csrf_exempt
def handlerequest(request):
    # paytm send post request
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print("order unsuccessful because" + respons_dict['RESPMSG'])
    return render(request, 'pages/paymentstatus.html',
                  {'response': response_dict})
    # return HttpResponse('Done')


def elements(request):
    return render(request, 'pages/elements.html',
                  {"BASE_URL": settings.BASE_URL})


def confirmation(request):
    return render(request, 'pages/confirmation.html',
                  {"BASE_URL": settings.BASE_URL})
