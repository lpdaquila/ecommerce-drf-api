from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

class Payment(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Payment')
