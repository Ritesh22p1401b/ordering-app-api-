from .models import Order
from rest_framework import serializers


class OrderCreateSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=50)
    order_status=serializers.HiddenField(default='PENDING')
    quantity=serializers.IntegerField()

    class Meta:
        model=Order
        fields=['size','order_status','quantity']
