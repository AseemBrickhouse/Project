from ..serializers import *
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
            to_user_json = AccountSerializer(to_user).data

            current_user_json = AccountSerializer(current_user).data

            request_json = FriendsRequestSerializer(request).data

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

        queryset = {}

        for account in obj.friends.all():
            account_json = AccountSerializer(account).data
            queryset[account_json['key']] = account_json
            queryset[account_json['key']]['is_friend'] = True


        return Response(queryset)

class AcceptFriendRequest(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        def addToFriends(current_user, from_user):
            print(Friends.objects.filter(account=from_user))
            if not Friends.objects.filter(account=from_user):
                list = Friends.objects.create(account=from_user)
                list.save()
            FU_list = Friends.objects.get(account=from_user)
            FU_list.friends.add(current_user)
            FU_list.save()

        try:
            #Fix later
            from_user = Account.objects.get(key=request.data['key'])
            #Catch Error
            print(from_user, current_user)
            friend_request = FriendRequest.objects.all().get(from_user=from_user, to_user=current_user)
            if not Friends.objects.filter(account=current_user):
                list = Friends.objects.create(account=current_user)
                list.save()

            list = Friends.objects.get(account=current_user)
            list.friends.add(from_user)
            
            list.save()
            queryset = {}

            #Add current user as a friend for the friend searching
            addToFriends(current_user, from_user)
            
            for friend in list.friends.all():
                print(friend)
                friend_json = AccountSerializer(friend).data
                queryset[friend_json['key']] = friend_json

            #Accepted request of both sides so we delete
            friend_request.delete()

            return Response(queryset)

        except FriendRequest.DoesNotExist:
            return Response({
                "Message": "Err"
            })