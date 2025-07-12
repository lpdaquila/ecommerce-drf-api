from rest_framework.views import APIView
from apps.products.models import Product, ProductVariant, VariationOption, Price

class Base(APIView):
    def get_product(self, slug: str):
        query = """
        SELECT p.id, p.name, pr.price 
FROM products_product p
JOIN products_productvariant v ON v.product_id = p.id
JOIN products_price pr ON pr.product_var_id = v.id
WHERE p.slug = %s
        """