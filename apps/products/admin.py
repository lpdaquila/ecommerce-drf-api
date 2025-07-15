from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Product, Variation, SubVariation, Price, PriceType, SubVariationType, Category

class ProductVarInline(admin.TabularInline):
    model = Variation
    extra = 1
    autocomplete_fields = ['options']
    
@admin.register(SubVariation)
class SubVariationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    inlines = [ProductVarInline,]
    
@admin.register(PriceType)
class PriceTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

    
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'currency')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    
@admin.register(SubVariationType)
class SubVariationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)
