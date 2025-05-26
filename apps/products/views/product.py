from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.products import models

class ProductList(ListView):
    model = models.Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 3
    
class ProductDetails(DetailView):
    model = models.Product
    template_name = 'product/details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'