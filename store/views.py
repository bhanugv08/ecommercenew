from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import *


# Create your views here.
def Register(request):
    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        usn=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        print("user created")
        usn.save()
        return HttpResponse("successfully created")
    else:
        return render(request,"store/register.html")

def login_request(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            return HttpResponse("invalid credentials")
    else:
        return render(request,'store/login.html')


def store(request):
    product=Product.objects.all()
    return render(request, 'store/store.html', {'product':product})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total':0, 'get_cart_items' :0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items':items,'order':order}
    return render(request, 'store/checkout.html', context)
