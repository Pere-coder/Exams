from rest_framework import serializers
from .models import NewUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'user_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    
