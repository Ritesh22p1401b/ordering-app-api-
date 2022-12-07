from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *

User=get_user_model()

class OrderCreateListView(generics.GenericAPIView):

    serializer_class=OrderCreateSerializer
    queryset=Order.objects.all()
    permission_classes=[IsAuthenticated]

    def get(self,request):

        orders=Order.objects.all()
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


    def post(self,request):

        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    serializer_class=OrderDetailSerializer
    permission_classes=[IsAuthenticated]


    def get(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,order_id):
        order =get_object_or_404(Order,id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class=UpdateOderStatusSeriailizer

    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserOrderView(generics.GenericAPIView):
    serializer_class=OrderDetailSerializer

    def get(self,request,user_id):
        user=get_object_or_404(User,pk=user_id)
        order=Order.objects.all().filter(customer=user)
        serializer=self.serializer_class(instance=order,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class UserOrderDetailView(generics.GenericAPIView):
    serializer_class=OrderDetailSerializer

    def get(self,request,user_id,order_id):
        user=get_object_or_404(User,pk=user_id)
        order=Order.objects.all().filter(customer=user).filter(pk=order_id)
        serializer=self.serializer_class(instance=order,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
