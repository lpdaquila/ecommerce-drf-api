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
    short_description = models.CharField(max_length=400)
    long_description = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
class ProductVariant(models.Model):
    """
    #### ProductVariant
        product - FK Product
        sku - Char
        options - MtM VariationOption
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100, unique=True)
    options = models.ManyToManyField('VariationOption')
    
class VariationOption(models.Model):
    variation = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    
class PriceType(models.Model):
    name = models.CharField(max_length=100)
    
class Price(models.Model):
    """
    #### Price table
        price - float
        currency - char
    """
    price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)