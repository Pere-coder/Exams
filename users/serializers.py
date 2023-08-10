from rest_framework import serializers
from .models import NewUser
from django.contrib.auth import  authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'user_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
   