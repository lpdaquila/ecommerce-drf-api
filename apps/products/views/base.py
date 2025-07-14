from rest_framework.views import APIView

from apps.products.models import Product
from apps.utils.query_handler import load_query, use_cursor
from apps.utils.exceptions import ProductNotFound

class Base(APIView):
    def get_products(self):
        query = load_query('apps/products/sql/get_products.sql')
        result = use_cursor(query)
        return result
        
    def get_product_variant(self, product_id):
        query = load_query('apps/products/sql/get_product_variant.sql')
        result = use_cursor(query, [product_id])
        return result
        
    def get_a_product(self, slug):
        product = Product.objects.filter(slug=slug)\
            .values(
                'id', 
                'slug', 
                'name', 
                'short_description', 
                'long_description'
            ).first()
            
        if not product:
            raise ProductNotFound
            
        return product