from django.db import connection

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Product
from apps.utils.load_query import load

class Base(APIView):
    def get_products(self):
        query = load('apps/products/sql/get_products.sql')
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description] # type: ignore
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        
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
            return Response({"detail": "Product not found"}, status=404)
            
        return product
    
    def get_product_variant(self, product_id):
        query = load('apps/products/sql/get_product_variant.sql')
        with connection.cursor() as cursor:
            cursor.execute(query, [product_id])
            columns = [col[0] for col in cursor.description] # type: ignore
            return [dict(zip(columns, row)) for row in cursor.fetchall()]