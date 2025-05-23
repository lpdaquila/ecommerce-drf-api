from django.contrib import admin

from .models import Product, Variation

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'get_price', 'get_promotional_price')
    inlines = [VariationInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
