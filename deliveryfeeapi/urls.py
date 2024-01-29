from django.urls import path
from .views import calculate_delivery_fee_api

urlpatterns = [
    path('calculate_delivery_fee_api/', calculate_delivery_fee_api, name='calculate_delivery_fee_api'),
]