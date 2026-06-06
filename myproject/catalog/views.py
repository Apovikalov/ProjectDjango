# catalog/views.py
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.models import Product
from catalog.forms import ProductForm
from catalog.services import ProductService
from unicodedata import category


class BaseView(TemplateView):
    template_name = 'catalog/base.html'


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        queryset = cache.get('all_products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('all_products_queryset', queryset, 60 * 15)
        return queryset


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductFormView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
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


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.object.id
        context['product_list'] = ProductService.get_products_by_category(category_id)
        return context


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('products.delete_product'):
            return HttpResponseForbidden('У Вас нет прав на удаление продукта.')

        product.delete()

        return redirect('products:product_list')


class UnpublishProductView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('products.can_unpublish_product'):
            return HttpResponseForbidden('Вы не можете снять продукт с публикации.')

        product.publish_status = False
        product.save()

        return redirect('products:product_list')

    def test_func(self):
        user = self.request.user
        product = self.get_object()
        return user == product.owner or user.has_perm('products.can_unpublish_product')
