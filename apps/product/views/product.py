from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

class ProductList(ListView):
    ...
    
class ProductDetails(View):
    ...