# catalog/views.py
from django.shortcuts import render

from catalog.models import Category, Product


# from django.http import HttpResponse


def home(request):
    product = Product.objects.get(name='Продукт 1')
    context = {'product': product, 'all_products': Product.objects.all()}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):
    product = Product.objects.get(name='Продукт 1')
    context = {'product': product, 'all_products': Product.objects.all()}
    return render(request, 'catalog/products.html', context)
