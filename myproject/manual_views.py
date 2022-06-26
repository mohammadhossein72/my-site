import imp
from django.http import HttpResponse


def raf_func(request):
    return HttpResponse('Hello')