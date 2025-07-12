from apps.products.views.base import Base
from apps.products.serializers import ProductsSerializer


from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class Products(Base):
    permission_classes = [AllowAny]
    def get(self, _request):
        products = self.get_products()
        
        serializer = ProductsSerializer(products, many=True)
        
        return Response({"products": serializer.data})



