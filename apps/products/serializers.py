from rest_framework import serializers

from apps.products.models import Product, Price

class ProductsSerializer(serializers.ModelSerializer):
    sale_price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        allow_null=True, 
        required=False
    )
    
    promo_price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        allow_null=True, 
        required=False
    )
    
    class Meta:
        model = Product
        fields = (
            'id',
            'slug',
            'name',
            'sale_price',
            'promo_price',
        )