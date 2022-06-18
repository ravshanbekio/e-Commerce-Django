from django.urls import path
from base.views import DashboardView, AboutView, DeliveryView, LocationView, ProductDetailView

urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard'),
    path('about/',AboutView.as_view(), name='about'),
    path('delivery/',DeliveryView.as_view(), name='delivery'),
    path('location/',LocationView.as_view(), name='location'),
    path('product/<category>/<title>/',ProductDetailView.as_view(), name='product-detail'),
]