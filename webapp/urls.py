from django.urls import path

from webapp.views import raf_func



urlpatterns = [

    # path('url address', 'view')
    path('raf-add',raf_func)
]