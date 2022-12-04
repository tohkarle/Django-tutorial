from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.

# /products -> index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# /products/cart -> cart
def cart(request):
    return HttpResponse("Cart Page")