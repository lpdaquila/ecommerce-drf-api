from django.db import models

class Product(models.Model):
    """
    #### Product
        name - char
        short_description - char
        long_description - char
        slug - slug
    """
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=400, blank=True, null=True)
    long_description = models.CharField(max_length=2000, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
class Variation(models.Model):
    """
    #### Variation
        product - FK Product
        sku - Char
        options - MtM VariationOption
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100, unique=True)
    options = models.ManyToManyField('SubVariation')
    
    def __str__(self) -> str:
        return f"{self.sku} - {self.product.name}"
    
class SubVariation(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class PriceType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Price(models.Model):
    """
    #### Price table
        price - float
        currency - char
    """
    price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE)
    product_var = models.ForeignKey(Variation, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    
    def __str__(self) -> str:
        return f"{self.price_type.name} - {self.price}"