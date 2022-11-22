from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView    
from datetime import datetime
from backend.AllViews.Util.ChatroomUtil import *
import random
import string
import os

class SendFriendRequest(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        to_user = None

        try:
            to_user = Account.objects.all().get(key=request.data['key'])

        except Account.DoesNotExist:
            return Response({
                "Message": "User to send request to does not exists"
            })
        
        request = FriendRequest.objects.all().filter(from_user=current_user, to_user=to_user)

        if not request:
            request = FriendRequest.objects.create(
                from_user=current_user,
                to_user=to_user,
            )
            request.save()
            return Response({
                "Message": "Request succesfully sent"
            })
        else:
            return Response({
                "Message": "Request already exists"
            })

class GetAllRequest(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        queryset = FriendRequest.objects.all().filter(to_user=current_user)

        if not queryset:
            return Response({
                "Message": "You currently have no friend requests"
            })
        
        current_request = {}
        for request in queryset:
            to_user = Account.objects.all().get(key=to_user.key)
            to_user_json = AccountSerilizer(to_user).data

            current_user_json = AccountSerilizer(current_user).data

            request_json = FriendsRequestSerilizer(request).data

            current_request[request_json['id']] = request_json
            current_request[request_json['id']]['from_user'] = current_user_json
            current_request[request_json['id']]['to_user'] = to_user_json

        return Response(current_request)

class GetAllFriends(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        obj = None
        try:
            obj = Friends.objects.all().get(account=current_user)
        except Friends.DoesNotExist:
            return Response({
                "Message": "You currently have no friends."
            })

        list = obj.friends.all()
        queryset = {}

        for account in obj.friends.all():
            account_json = AccountSerilizer(account).data
            queryset[account_json['key']] = account_json
            queryset[account_json['key']]['is_friend'] = True


        return Response(queryset)