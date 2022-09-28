from rest_framework import serializers
from app_1.models import UserProfile, Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"
        

class UserProfileSerializer(serializers.ModelSerializer):
    payment_by = BalanceSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password', 'payment_by')
        extra_kwargs = {'password':{'write_only':True}}
        
        def create(self,validated_data):
            user = UserProfile(
                email=validated_data['email'],
                name=validated_data['name'],
            )
            
            user.set_password(validated_data['password'])
            user.save()
            
            return user