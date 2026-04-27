# catalog/views.py
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# from django.http import HttpResponse


def base(request):
    return render(request, 'catalog/base.html')


def home(request):
    product = Product.objects.get(name='Продукт 1')
    context = {'product': product, 'all_products': Product.objects.all()}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):
    product = Product.objects.get(name='Продукт 1')
    context = {'product': product}
    return render(request, 'catalog/products.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/products.html', context)
