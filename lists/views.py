from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    """home page"""
    return HttpResponse('<html><title>To-Do lists</title></html>')
