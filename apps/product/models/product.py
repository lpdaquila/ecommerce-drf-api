from django.db import models
from django.utils.text import slugify
from apps.utils import resize_image

class Product(models.Model):
    """
    Product:
            Product:
                name - Char
                short_description- Text
                long_description - Text
                image - Image
                slug - Slug
                marketing_price - Float
                marketing_promotional_price - Float
                product_type - Choices
                    ('V', 'Variable'),
                    ('S', 'Simple'),

    """
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(
        upload_to='products/%Y/%m/', 
        blank=True, 
        null=True
    ) #TODO: remove blank and null for production
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    marketing_price = models.FloatField()
    marketing_promotional_price = models.FloatField(default=0.0)
    product_type = models.CharField(
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        ),
        default='S'
    )
    
    def get_price(self):
        return f'{self.marketing_price:.2f} BRL'
    get_price.short_description = 'Price' # type: ignore
    
    def get_promotional_price(self):
        return f'{self.marketing_promotional_price:.2f} BRL'
    get_promotional_price.short_description = 'Promo Price' # type: ignore
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
        super().save(*args, **kwargs)
        
        max_image_size = 800
        
        if self.image:
            resize_image(self.image, max_image_size)
    
    def __str__(self) -> str:
        return self.name
    
class Variation(models.Model):
    """ Variation:
                name - char
                product - FK Product
                price - Float
                promotional_price - Float
                inventory - Int
                
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0.0)
    inventory = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name or self.product.name