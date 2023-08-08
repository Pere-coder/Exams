from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from .serializers import CustomUserSerializer


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(password=make_password(serializer.validated_data['password']))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        