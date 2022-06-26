from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def raf_func(request):
    return HttpResponse('Hello')