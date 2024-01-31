from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
import json


class DeliveryFeeView(object):
    """This module contains keywords to saveRole configuration using Rest API calls"""

    def __init__(self):
        self.base_fee = 200
        self.additional_distance_fee_per_increment = 100
        
    def calculate_delivery_fee(self, cart_value: str, delivery_distance, number_of_items, time):
        '''
        Function to calculate item deleivery fee 
        :param cart_value: int
        :param delivery_distance: int
        :param number_of_items: int
        :param time: str
        :return: int
        '''
        
        # small order surcharge
        # non-negative (using max function)
        small_order_surcharge = max(0, 1000 - cart_value)
        
        #extra_distance_charge
        additional_distance = max(0, delivery_distance - 1000)
        
        increments = (additional_distance + 500 -1 ) // 500
        
        additional_distance_fee = increments * self.additional_distance_fee_per_increment
        
        total_distance_fee = self.base_fee + additional_distance_fee
        
        
        #item surcharge
        item_difference = max(0, number_of_items - 4)
        items_surcharge = 0
        bulk_fee = 120
        
        if number_of_items > 4:
            items_surcharge = item_difference * 50
            
        if number_of_items > 12:
            items_surcharge += bulk_fee
            
        
        total_fee = total_distance_fee + small_order_surcharge + items_surcharge 
        
        # delivery discount based on cart_value
        if cart_value >= 2000:
            total_fee = 0
            
        # checking for rush hour 
        if self.is_rush_hour(time):
            total_fee *= 1.2
            
        total_fee = int(total_fee)
        
        # Ensure the total fee does not exceed 15
        total_fee = min(total_fee, 1500)
        
        return total_fee
        
        
    def is_rush_hour(self, time):
        order_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
        
        # check for friday
        is_friday = order_time.weekday() == 4
        
        # check time on friday
        is_between_15_and_19 = 15 <= order_time.hour < 19
        
        if is_friday and is_between_15_and_19:
            return True
        else: 
            return False
        
    @csrf_exempt
    def calculate_delivery_fee_api(self, request):
        '''
        
        :param request: 
        :return: 
        '''
        try:
            data = json.loads(request.body.decode('utf-8'))
            cart_value = data.get('cart_value', 0)
            delivery_distance = data.get('delivery_distance', 0)
            number_of_items = data.get('number_of_items', 0)
            time = data.get('time', '')
            
            if 'Z' in time:
                time = time.rstrip('Z')
            
            parsed_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
            
            Order.objects.create(
                cart_value = cart_value,
                delivery_distance = delivery_distance,
                number_of_items = number_of_items,
                time = parsed_datetime
            )
            
            
            delivery_fee = self.calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time)
            
            return JsonResponse({"delivery_fee": delivery_fee})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    
    
        
        
    
    
    
    
    