from .models import Order
from rest_framework import serializers


class OrderCreateSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=50,default='SMALL')
    order_status=serializers.HiddenField(default='PENDING')
    quantity=serializers.IntegerField()

    class Meta:
        model=Order
        fields=['id','size','order_status','quantity']

class OrderDetailSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=50)
    order_status=serializers.CharField(default='PENDING')
    quantity=serializers.IntegerField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()

    class Meta:
        model=Order
        fields=['id','size','order_status','quantity','created_at','updated_at']

class UpdateOderStatusSeriailizer(serializers.ModelSerializer):
    order_status=serializers.CharField(default='PENDING')

    class Meta:
        model=Order
        fields=['order_status']
