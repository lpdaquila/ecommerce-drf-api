from django.db import connection

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import ProductVariant
from apps.utils.load_query import load

class Base(APIView):
    def get_products(self):
        query = load('apps/products/sql/get_products.sql')
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description] # type: ignore
            return [dict(zip(columns, row)) for row in cursor.fetchall()]