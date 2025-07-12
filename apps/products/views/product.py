from apps.products.views.base import Base
from apps.products.serializers import (
    ProductsSerializer, ProductDetailSerializer,
    ProductVariantSerializer
    )


from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class Products(Base):
    permission_classes = [AllowAny]
    def get(self, _request):
        products = self.get_products()
        
        serializer = ProductsSerializer(products, many=True)
        
        return Response({"products": serializer.data})
    
class ProductDetail(Base):
    permission_classes = [AllowAny]
    
    def get(self, _request, slug):
        product = self.get_a_product(slug)
        
        variants = self.get_product_variant(product.get('id')) # type: ignore
        
        product['variants'] = variants # type: ignore
        
        serializer = ProductDetailSerializer(product)
        
        return Response({"product": serializer.data,})
        
        



