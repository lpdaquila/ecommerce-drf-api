from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
    
class AddCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('add cart')
    
class RemoveCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('remove cart')
    
class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('cart')