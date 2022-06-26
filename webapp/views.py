from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def raf_func_one(request):
    return HttpResponse('Hello')

def raf_func_two(request):
    return HttpResponse('Bye')