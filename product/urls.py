from django.urls import path
from product.views import *

urlpatterns = [
    path('',BuyProductView.as_view(), name='box'),
    path('add-product/<category>/<title>',AddtoBoxView.as_view(), name='add-box'),
]