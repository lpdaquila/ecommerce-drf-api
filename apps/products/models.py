from uuid import uuid4
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    #### Category
        name - Char
        parent - 'self' FK
        slug - Slug
    """
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        related_name='children', 
        on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def get_full_path(self):
        path = []
        category = self
        while category:
            path.insert(0, category)
            category = category.parent
        return path
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid4().hex[:4]}"
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    #### Product
        name - char
        category - FK Category
        short_description - char
        long_description - char
        slug - slug
    """
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        related_name='products',
        null=True
    )
    short_description = models.CharField(max_length=400, blank=True, null=True)
    long_description = models.CharField(max_length=2000, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid4().hex[:6]}"
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
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
    
class SubVariationType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class SubVariation(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        SubVariationType, 
        on_delete=models.CASCADE,
        related_name='subvariation'
    )
    
    def __str__(self):
        return f"{self.name} - ({self.type})"
    
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
    