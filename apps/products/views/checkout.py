from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class Checkout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('checkout')