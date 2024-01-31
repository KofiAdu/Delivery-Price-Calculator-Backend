from django.urls import path
from deliveryfeeapi.views import DeliveryFeeView

#create an isnstance of the DeliveryFeeView
delivery_fee_view = DeliveryFeeView()

urlpatterns = [
    path('calculate_delivery_fee_api/', delivery_fee_view.calculate_delivery_fee_api, name='calculate_delivery_fee_api'),
]