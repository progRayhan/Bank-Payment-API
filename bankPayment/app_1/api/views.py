from datetime import datetime
from app_1.models import UserProfile, Balance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_1.models import UserProfile, Balance
from app_1.api.serializers import UserProfileSerializer, BalanceSerializer

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
payment_time = dt_string[11:-1]

class UserListAV(APIView):
    def get(self, request):
        try:
            userName = UserProfile.objects.all()
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(userName, many=True)
        return Response(serializer.data)
    
class UserDetailAV(APIView):
    def get(self, request, pk):
        try:
            userName = UserProfile.objects.all()
        except UserProfile.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(userName)
        return Response(serializer.data)
    

class BalanceListAV(APIView):
    def get(self, request):
        balance = Balance.objects.all()
        serializer = BalanceSerializer(balance, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BalanceSerializer(data=request.data)
        
        if payment_time >= "09:00:00" and payment_time <= "11:00:00":
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'error' : 'bank is closed'}, status=status.HTTP_404_NOT_FOUND)
    
class BalanceDetailAV(APIView):
    def get(self, request,pk):
        try:
            balance = Balance.objects.get(pk=pk)
        except Balance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BalanceSerializer(balance)
        return Response(serializer.data)
    
    