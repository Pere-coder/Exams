from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .serializers import CustomUserSerializer
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.authtoken.models import Token
from .models import NewUser
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(password=make_password(serializer.validated_data['password']))
        user = NewUser.objects.get(user_name=serializer.validated_data['user_name'])
        # token = Token.objects.create(user=user)
        return Response({"user":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(NewUser, user_name = request.data['user_name'])
    if not user.check_password(request.data['password']):
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    # token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(instance=user)
    return Response({"user":serializer.data}, status=status.HTTP_202_ACCEPTED)


   