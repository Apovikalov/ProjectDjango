from catalog.models import Category, Product

class ProductService:

    @staticmethod
    def get_products_by_category(category_id):
        category = Category.objects.get(id=category_id)
        product_list = Product.objects.filter(category=category)
        return product_list
