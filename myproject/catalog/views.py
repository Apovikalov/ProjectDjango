# catalog/views.py
from django.views.generic import DetailView, ListView, TemplateView
# from django.shortcuts import render, get_object_or_404

from catalog.models import Product


class BaseView(TemplateView):
    template_name = 'catalog/base.html'


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'all_products'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# def base(request):
#     return render(request, 'catalog/base.html')


# def home(request):
#     product = Product.objects.get(name='Продукт 1')
#     context = {'product': product, 'all_products': Product.objects.all()}
#     return render(request, 'catalog/home.html', context)


# def contacts(request):
#     return render(request, 'catalog/contacts.html')


# def product_detail(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     context = {'product': product}
    #     return render(request, 'catalog/product_detail.html', context)


# def products(self, request):
    #     product = Product.objects.get(name='Продукт 1')
    #     context = {'product': product}
    #     return render(request, 'catalog/product_detail.html', context)
