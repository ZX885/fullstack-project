from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    password2 = request.data.get('password2')
    if password != password2:
        return Response({'error': 'Passwords do not match'}, status=400)
    if not username or not password:
        return Response({'error': 'Please provide both username and password'}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=400)
    if not email:
        return Response({'error': 'Email is required'}, status=400)
    user = User.objects.create_user(username=username, password=password, email=email)
    Token.objects.create(user=user)
    return Response({'token': user.auth_token.key}, status=201)




# {
#     "username":"test",
#     "email":"test@gmail.com",
#     "password":"test",
#     "password2":"test2"
# }


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMTc4MjUwNCwiaWF0IjoxNzAxNjk2MTA0LCJqdGkiOiJmNTg4MzVhOWE4MWY0ZjI3YmE1MjAwZTA4MGI4NmI0NyIsInVzZXJfaWQiOjF9.NIHfjygP3Pgv03e4Rq4mWdCWtEQbMHglt-XyyA8c-PE",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNzAzMzA0LCJpYXQiOjE3MDE2OTYxMDQsImp0aSI6IjBmMzM5MDIzM2YzYzRiZjJiYzY4MTBiYzcwYjgwYWQ4IiwidXNlcl9pZCI6MX0.I-KLEMTwSOaIo214r-zs0dE8PaNL_jiwDpzq_oei0Ck"
# }