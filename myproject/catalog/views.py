# catalog/views.py
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from django.shortcuts import render, get_object_or_404, redirect

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'price', 'created_at', 'last_changed_at']
    template_name = "catalog/product_edit.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy('home')


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('products.delete_product'):
            return HttpResponseForbidden('У Вас нет прав на удаление продукта.')

        product.delete()

        return redirect('products:product_list')


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('products.can_unpublish_product'):
            return HttpResponseForbidden('Вы не можете снять продукт с публикации.')

        product.publish_status = False
        product.save()

        return redirect('products:product_list')


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
