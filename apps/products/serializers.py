from rest_framework import serializers

from apps.products.models import Product

class ProductsSerializer(serializers.ModelSerializer):
    sub_vars = serializers.JSONField()
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
            'sub_vars'
        )
        
class ProductVariantSerializer(serializers.Serializer):
    variant_id = serializers.IntegerField()
    sku = serializers.CharField()
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
    sub_vars = serializers.JSONField()
        
class ProductDetailSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'slug',
            'name',
            'short_description',
            'long_description',
            'variants'
        )


    
    
    