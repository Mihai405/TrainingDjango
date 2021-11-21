from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import FriendSerializer
from .models import Friend
from rest_framework import status
from apps.users.models import User
import jwt

class FriendsView(viewsets.ModelViewSet):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class APIListFriendsView(APIView):

    def get(self,request):
        friends_list=[]
        token=request.session.get('user',None)
        if not token:
            return Response("Unauthenticated",status=status.HTTP_405_METHOD_NOT_ALLOWED)
        decode_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        user=User.objects.get(id=decode_token['id'])
        for friend in Friend.objects.filter(user=user):
            serializer=FriendSerializer(friend)
            friends_list.append(serializer.data)
        return Response(friends_list)

    def post(self,request):
        token = request.session.get('user', None)
        if not token:
            return Response("Unauthenticated", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        decode_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        user = User.objects.get(id=decode_token['id'])
        serializer=FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class APIAddFriendView(APIView):

    def post(self,request):
        token = request.session.get('user', None)
        if not token:
            return Response("Unauthenticated", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        decode_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        user = User.objects.get(id=decode_token['id'])
        serializer=FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class APIUpdateFriendView(APIView):
    def put(self,request,pk):
        token = request.session.get('user', None)
        if not token:
            return Response("Unauthenticated", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        decode_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        user = User.objects.get(id=decode_token['id'])
        try:
            friend=Friend.objects.get(id=pk)
        except Friend.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer=FriendSerializer(friend,data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        token = request.session.get('user', None)
        if not token:
            return Response("Unauthenticated", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            friend=Friend.objects.get(id=pk)
        except Friend.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            friend.delete()
            return Response({"Delete":"Success"},status=status.HTTP_204_NO_CONTENT)

class APIDeleteFriendView(APIView):
    def delete(self,request,pk):
        token = request.session.get('user', None)
        if not token:
            return Response("Unauthenticated", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            friend=Friend.objects.get(id=pk)
        except Friend.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            friend.delete()
            return Response({"Delete":"Success"},status=status.HTTP_204_NO_CONTENT)