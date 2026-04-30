# catalog/urls.py
from django.urls import path
from .views import BaseView, ProductDetailView

urlpatterns = [
    path('base/', BaseView.as_view(), name='base'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
