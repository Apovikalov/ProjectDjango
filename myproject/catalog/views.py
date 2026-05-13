# catalog/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView
# from django.shortcuts import render, get_object_or_404

from catalog.models import Product
from catalog.forms import ProductForm


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


class ProductFormView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')


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
