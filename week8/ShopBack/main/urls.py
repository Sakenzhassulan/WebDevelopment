from django.urls import path
from main.views import hello, product_list, product_detail

urlpatterns=[
    path('hello/', hello),
    path('products/', product_list),
    path('products/<int:product_id>/',product_detail)
]