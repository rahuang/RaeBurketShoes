from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Test
from .models import ShoppingCart

import requests

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python Test1!')

def main(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'index.html', {"numItems": len(carts)})

def about(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'about.html', {"numItems": len(carts)})

def blog(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'blog.html', {"numItems": len(carts)})

def contact(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'contact.html', {"numItems": len(carts)})

def details(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'details.html', {"numItems": len(carts)})

def login(request):
    return render(request, 'login.html')

def products(request):
    carts = ShoppingCart.objects.all()
    return render(request, 'products.html', {"numItems": len(carts)})

def register(request):
    return render(request, 'register.html')

def landing(request):
    return render(request, 'landing.html')

def cart(request):
    if request.method == 'POST':
        if 'pic' in request.POST:
            cart = ShoppingCart(pic=request.POST['pic'], name=request.POST['name'], price=request.POST['price'])
            cart.save()
        elif 'id' in request.POST:
            ShoppingCart.objects.filter(id=request.POST['id']).delete()

    carts = ShoppingCart.objects.all()
    l = []
    temp = []
    for i in xrange(len(carts)):
        temp.append(carts[i])
        if(i%3 == 2):
            l.append(temp)
            temp = []
    if(temp != []):
        l.append(temp)

    length = len(carts)
        
    return render(request, 'cart.html', {"carts": l, "numItems": length})

def test(request):
    test = Test(name="hello")
    test.save()

    test = Test.objects.all()
    return render(request, 'db.html', {'greetings': test})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

