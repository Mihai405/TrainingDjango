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

#Use register view to list/create/update/delete a new user
class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

#The custom auth view will use sessions to identify the user
class AuthView(APIView):
    @swagger_auto_schema(operation_description="This API is used to Log In a user",
        request_body=LogInSerializer,responses={200:"{token:user token , email:user email}"})
    def post(self,request):
         #here the user logs in using his email and password and after that , a jwt_token based on his id
         #will be created and saved in sessions
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

    @swagger_auto_schema(operation_description="This API is used to Log Out a user")
    def delete(self,request):
        #here the user logs out , his token will be deleted from sessions and from cookies
        try:
            user = decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        delete_session_user(request)
        return Response("LogOut",status=status.HTTP_204_NO_CONTENT)
