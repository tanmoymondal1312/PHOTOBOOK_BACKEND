# accounts/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import CustomUser
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from twilio.rest import Client

@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User registered successfully!',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'User registered but authentication failed.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



