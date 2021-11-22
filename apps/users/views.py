from django.shortcuts import render
from rest_framework import viewsets
from .serializer import RegisterSerializer , LogInSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
from rest_framework.response import Response
from rest_framework.decorators import action

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LogInViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LogInSerializer


    @action(detail=False,methods=['post'])
    def login(self,request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid password")
        payload = {
            'id': user.id,
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        request.session["user"]=token
        return Response({"token": token,"email":user.email})
    @action(detail=False , methods=['post'])
    def logout(self,request):
        return Response("Clear Session")

class LogInView(APIView):
     def post(self,request):
         email      =   request.data['email']
         password   =   request.data['password']
         try:
            user   =   User.objects.get(email=email)
         except User.DoesNotExist:
             raise AuthenticationFailed('User not found')
         if not user.check_password(password):
             raise AuthenticationFailed("Invalid password")
         payload={
            'id':user.id,
         }
         token = jwt.encode(payload, 'secret', algorithm='HS256')
         request.session["user"] = token
         decode_token = jwt.decode(token,'secret',algorithms=["HS256"])
         return Response({"token":request.session["user"]})
