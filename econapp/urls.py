from django.urls import path
from .views import *

urlpatterns = [
    path('category/<category_slug>/', category_view, name='category_detail'),
    path('product/<product_slug>/', product_view, name='product_detail'),
    path('', base_view, name='base')
]
