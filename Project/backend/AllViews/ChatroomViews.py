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


class APITEST(APIView):
    def post(self, request, *args, **kwargs):
        def getParentDir(CurrentPath, levels = 1):
            current_new = CurrentPath
            for i in range(levels + 1):
                current_new = os.path.dirname(current_new)
            
            return os.path.relpath(CurrentPath, current_new)


        par = "Chatroom"
        directory = "Logs"
        par_path = os.path.join(par, directory)
        path = os.path.join(getParentDir(os.getcwd(), 0), par_path)

        random_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        file_path = os.path.join(path, random_id)

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        file_path = os.path.join(file_path, random_id)
        make_file = open(file_path, "a")
        make_file.close()

        print(file_path)
        return Response(request.data)

class GetAllMessages(APIView):
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
    We should have the studygroup id
    from here we can get the chat id
    then create the message in the database
    then open the file and write a new entry
    """
    def post(self, request, *args, **kwargs):
        
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.get(studygroup_id = request.data['studygroup_id'])
        print(studygroup)

        chat = studygroup.chat_id
        print(chat)

        message = Message.objects.create(
            message_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            chatroom_id = chat,
            account = current_user,
            content = request.data['message']
        )
        message.save()
        person = current_user.first_name + " " + current_user.last_name
        create(studygroup.studygroup_id, person, chat.chatroom_id, request.data['message'])

        return Response(request.data)

class DeleteMessage(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        pass

class GetUserMessages(APIView):
    def post(self, request, *args, **kwargs):
        pass

class GetCurrentUserMessages(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        queryset = {}

        for message in Message.objects.all().filter(account=current_user):
            message_json = MessageSerilizer(message).data
            queryset[message_json['message_id']] = message_json

            account_json = AccountSerilizer(current_user).data

            queryset[message_json['message_id']]['account'] = account_json

        return Response(queryset)