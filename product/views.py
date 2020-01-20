from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, "product/products.html", {'products':products})