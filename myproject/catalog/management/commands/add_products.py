from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()  # Удаляем существующие записи
        Category.objects.all().delete()  # Удаляем существующие записи

        category, _ = Category.objects.get_or_create(name='Категория 1')

        products = [
            {'name': 'Продукт 1', 'category': category, 'price': 10.00,
             'created_at': '2026-1-1', 'last_changed_at': '2026-1-1'},
            {'name': 'Продукт 2', 'category': category, 'price': 20.00,
             'created_at': '2026-1-1', 'last_changed_at': '2026-1-1'},
            {'name': 'Продукт 3', 'category': category, 'price': 30.00,
             'created_at': '2026-1-1', 'last_changed_at': '2026-1-1'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}'))
