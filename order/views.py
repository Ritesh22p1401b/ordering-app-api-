from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import OrderCreateSerializer
from rest_framework.permissions import IsAuthenticated
from .models import *


class OrderCreateListView(generics.GenericAPIView):

    serializer_class=OrderCreateSerializer
    queryset=Order.objects.all()

    def get(self,request):

        orders=Order.objects.all()
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        user=request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):

    def get(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass
