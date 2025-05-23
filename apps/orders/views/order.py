from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

class Checkout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Checkout order ok')

class Details(View):
    pass