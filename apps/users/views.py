from django.shortcuts import render
from rest_framework import viewsets
from .serializer import RegisterSerializer , LogInSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from custom.auth import encode_session_user,decode_session_user,delete_session_user
from rest_framework import exceptions
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LogInView(APIView):
    @swagger_auto_schema(operation_description="This API is used to Log In a user",
        request_body=LogInSerializer,responses={200:"{token:user token , email:user email}"})
    def post(self,request):
         email      =   request.data['email']
         password   =   request.data['password']
         try:
            user   =   User.objects.get(email=email)
         except User.DoesNotExist:
             raise AuthenticationFailed('User not found')
         if not user.check_password(password):
             raise AuthenticationFailed("Invalid password")
         token = encode_session_user(request, user.id)
         return Response({"token": token, "email": user.email})

class LogOutView(APIView):
    @swagger_auto_schema(operation_description="This API is used to Log Out a user")
    def delete(self,request):
        try:
            user = decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        delete_session_user(request)
        return Response("LogOut",status=status.HTTP_200_OK)
