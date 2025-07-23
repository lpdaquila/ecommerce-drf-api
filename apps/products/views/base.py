from rest_framework.views import APIView

from apps.products.models import Product, Category
from apps.utils.query_handler import load_query, use_cursor
from apps.utils.exceptions import ProductNotFound

class Base(APIView):
    def get_products(self):
        query = load_query('apps/products/sql/get_products_v2.sql')
        result = use_cursor(query, many=True)
        return result
        
    def get_product_detail(self, slug):
        query = load_query('apps/products/sql/get_product_variant_v2.sql')
        result = use_cursor(query, [slug])
        return result
    
    def get_product_categories(self, product_id):
        product = Product.objects.get(id=product_id)
        
        category_path = product.category.get_full_path() # type: ignore
        
        return category_path
        
        
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