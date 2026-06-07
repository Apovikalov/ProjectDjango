# catalog/urls.py
from django.urls import path
from .views import (BaseView, ContactsView, HomeView,
                    ProductDeleteView, ProductDetailView, ProductFormView, ProductUpdateView)

urlpatterns = [
    path('base/', BaseView.as_view(), name='base'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_form/', ProductFormView.as_view(), name='product_form'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
