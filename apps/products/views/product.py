from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

class ProductList(View):
    def get(self, *args, **kwargs):
        return HttpResponse('List')
    
class ProductDetails(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Details')