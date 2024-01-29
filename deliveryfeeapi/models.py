from django.db import models

# Create your models here.
class Order(models.Model):
    cart_value = models.IntegerField(null=True)
    delivery_distance = models.IntegerField(null=True)
    number_of_items = models.IntegerField(null=True)
    time = models.CharField(max_length=255, null=True)