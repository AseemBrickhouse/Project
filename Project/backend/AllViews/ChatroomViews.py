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



class GetAllMessages(APIView):
    """
    @ function
        Retrive all messages of current group
    @ request Params
        studygroup_id: request.data['studygroup_id']
    @ Return    
        All messages in group
    """
    def post(self, request, *args, **kwargs):

        studygroup = StudyGroup.objects.get(studygroup_id=request.data['studygroup_id'])
        chat = studygroup.chat_id

        queryset = {}

        for message in Message.objects.all().filter(chatroom_id=chat):
            message_json = MessageSerilizer(message).data
            queryset[message_json['message_id']] = message_json

            account = Account.objects.all().get(key=message.account.key)
            account_json = AccountSerilizer(account).data

            queryset[message_json['message_id']]['account'] = account_json
            queryset[message_json['message_id']]['studygroup_id'] = studygroup.studygroup_id

        return Response (queryset)

class CreateMessage(ObtainAuthToken):
    """
    @ function
        Given a user token, studygroup_id, and message, create a message for the group
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id']
        message: request.data['message]
    @ Return    
        Message telling whether or not the message was created
    """
    def post(self, request, *args, **kwargs):
        
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.get(studygroup_id = request.data['studygroup_id'])
        chat = studygroup.chat_id

        message = Message.objects.create(
            message_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            chatroom_id = chat,
            account = current_user,
            content = request.data['message']
        )
        message.save()
        person = current_user.first_name + " " + current_user.last_name
        create(studygroup.studygroup_id, person, chat.chatroom_id, request.data['message'])

        return Response({
            "Message": "Message successfully created."
        })

class UpdateMessage(ObtainAuthToken):
    """
    @ function
        Given a user token, studygroup_id, message id, and new message, update a message for the group
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id']
        message id: request.data['message_id']
        new_message : request.data['new_content']
    @ Return    
        Message telling whether or not the message was updated
    """
    def put(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.get(studygroup_id = request.data['studygroup_id'])
        chatroom = studygroup.chat_id

        try:
            message = Message.objects.all().get(account=current_user, message_id=request.data['message_id'])
            person = current_user.first_name + " " + current_user.last_name

            if request.data.__contains__('new_content'):
                update(studygroup.studygroup_id, person, chatroom.chatroom_id, message.content, request.data['new_content'])
                message.content = request.data['new_content']
                message.save(update_fields=['content'])
            else:
                return Response({
                    "Message": "Message to update is blank."
                })

            return Response({
                "Message": "Message has been succesfully updated."
            })
        except Message.DoesNotExist:
            return Response({
                "Message": "You are not the creator of the message or the message to update does not exists."
            })

class DeleteMessage(ObtainAuthToken):
    """
    @ function
        Given a user token, studygroup_id, message id, delete the message for the group
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id']
        message id: request.data['message_id']
    @ Return    
        Message telling whether or not the message was deleted
    """
    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.get(studygroup_id = request.data['studygroup_id'])
        chatroom = studygroup.chat_id

        try:
            message = Message.objects.all().get(account=current_user, message_id=request.data['message_id'])
            person = current_user.first_name + " " + current_user.last_name
            delete(studygroup.studygroup_id, person, chatroom.chatroom_id, message.content)

            message.delete()
            return Response({
                "Message": "Message has been succesfully deleted."
            })
        except Message.DoesNotExist:
            return Response({
                "Message": "You are not the creator of the message or the message to delete does not exists."
            })


class GetUserMessages(APIView):
    """
    @ function
        Given a studygroup_id, first_name, last_name, and email, retrieve all messages related to the person
    @ request Params
        studygroup id: request.data['studygroup_id']
        first_name: request.data['first_name']
        last_name: request.data['last_name']
        email: request.data['email']
    @ Return    
        All messages related to a user
    """
    def post(self, request, *args, **kwargs):
        studygroup = StudyGroup.objects.get(studygroup_id = request.data['studygroup_id'])
        chat = studygroup.id
        account = Account.objects.all().get(first_name=request.data['first_name'], last_name=request.data['first_name'], email=request.data['email'])
        queryset = {}
        messagees = Message.objects.all().filter(account=account, chatroom_id=chat)
        for message in messagees:
            message_json = MessageSerilizer(message).data
            queryset[message_json['message_id']] = message_json

            account_json = AccountSerilizer(account).data

            queryset[message_json['message_id']]['account'] = account_json

        return Response(queryset)

class GetCurrentUserMessages(ObtainAuthToken):
    """
    @ function
        Given a user token, studygroup_id, retrieve all messages from the current logged in user
    @ request Params
        user token: request.data['token']
        message id: request.data['message_id']
    @ Return    
        All messages related to current user
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        queryset = {}
        studygroup = StudyGroup.objects.get(studygroup_id = request.data['studygroup_id'])
        print(studygroup)
        chat = studygroup.chat_id
        print(chat)
        for message in Message.objects.all().filter(account=current_user, chatroom_id=chat):
            message_json = MessageSerilizer(message).data
            queryset[message_json['message_id']] = message_json

            account_json = AccountSerilizer(current_user).data

            queryset[message_json['message_id']]['account'] = account_json

        return Response(queryset)