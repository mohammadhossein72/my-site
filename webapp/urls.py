from django.urls import path

from webapp.views import raf_func_one , raf_func_two



urlpatterns = [

    # path('url address', 'view')
    path('raf-add-one',raf_func_one),

    path('raf-add-two',raf_func_two)
]