from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request,"index.html")

def index(request):
    return render(request, 'index.html')


def product_view(request):
    return render(request, 'products.html')

def About_view(request):
    return render(request, 'About.html')

def login_view(request):
    return render(request, 'login.html')

def Register_view(request):
    return render(request, 'Register.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def Cart_view(request):
    return render(request, 'Cart.html')

def Contact(request):
    return render(request, 'Contact.html')

def Details(request):
    return render(request, 'Details.html')


def thank(request):
    return render(request, 'thank.html')

def Account(request):
    return render(request, 'Account.html')

def Search(request):
    return render(request, 'Search.html')



def cart_view(request):
    book_name = "Treasure Island"  # Example book name
    book_price = 200  # Example book price
    context = {
        'book_name': book_name,
        'book_price': book_price
    }
    return render(request, 'cart.html', context)