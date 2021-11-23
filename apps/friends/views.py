from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import FriendSerializer
from .models import Friend
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from apps.users.models import User
from custom.auth import decode_session_user
from rest_framework import exceptions
from drf_yasg.utils import swagger_auto_schema

class FriendsView(viewsets.ModelViewSet):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

@method_decorator(cache_page(60*5), name='dispatch')
@method_decorator(vary_on_cookie,name='dispatch')
class APIFriendsView(APIView):

    @swagger_auto_schema(responses={200: FriendSerializer(many=True)})
    def get(self,request):
        try:
            user=decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        friends=Friend.objects.filter(user=user)
        serializer=FriendSerializer(friends,many=True)
        return Response(serializer.data)


    @swagger_auto_schema(request_body=FriendSerializer)
    def post(self,request):
        try:
            user=decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        serializer=FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@method_decorator(cache_page(60*5),name='dispatch')
@method_decorator(vary_on_cookie,name='dispatch')
class APIUpdateFriendView(APIView):

    @swagger_auto_schema(responses={200: FriendSerializer()})
    def get(self,request,pk):
        try:
            user = decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        try:
            friend=Friend.objects.get(id=pk)
        except Friend.DoesNotExist:
            return Response("Object not Found",status=status.HTTP_404_NOT_FOUND)
        serializer=FriendSerializer(friend)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: FriendSerializer()}, request_body=FriendSerializer)
    def put(self,request,pk):
        try:
            user = decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        try:
            friend = Friend.objects.get(id=pk)
        except Friend.DoesNotExist:
            return Response("Object not Found",status=status.HTTP_404_NOT_FOUND)
        serializer=FriendSerializer(friend,data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            user = decode_session_user(request)
        except exceptions.AuthenticationFailed:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        try:
            friend=Friend.objects.get(id=pk)
        except Friend.DoesNotExist:
            return Response("Object not Found",status=status.HTTP_404_NOT_FOUND)
        else:
            friend.delete()
            return Response({"Delete":"Success"},status=status.HTTP_204_NO_CONTENT)
