from rest_framework import generics,status
from rest_framework.response import Response


class User_Order(generics.GenericAPIView):
    def get(self,request):
        return Response({"message":"Order now"},status=status.HTTP_200_OK)
        





