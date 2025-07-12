from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Product, ProductVariant, VariationOption, Price, PriceType

class ProductVarInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    autocomplete_fields = ['options']
    
@admin.register(VariationOption)
class VariationOptionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    inlines = [ProductVarInline,]
    
@admin.register(PriceType)
class PriceTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

    
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'currency')

admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)
