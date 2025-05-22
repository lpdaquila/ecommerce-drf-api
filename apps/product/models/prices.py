from django.db import models
from apps.product.models.product import Product

class PriceType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class ProductPrice(models.Model):
    """
    ProductPrice:
                product - FK Product
                price_type - FK PriceType
                price - Float
                promotional_price - Float
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE)
    price = models.FloatField()
    
    def __str__(self) -> str:
        return f'{self.product.name} - {self.price_type.name}'