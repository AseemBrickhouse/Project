from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
import random
import string


class GetAllUserStudyGroups(ObtainAuthToken):
    """
    @ function
        Allows a user to request for all currently enrolled study gorups
    @ request Params
        user token: request.data['token']
    @ Return 
        queryset that contains all enrolled study groups along with their information
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        queryset = {}

        if StudyGroup.objects.all() == []:
            return Response({
                "Message": "You are not in any study groups currently"
        })

        for enroll in StudyEnroll.objects.all().filter(account=currentUser):
            enrollJSON = StudyEnrollSelizer(enroll).data
            #No need to try/except this because it should exist
            group = StudyGroup.objects.all().get(id=enrollJSON['studygroup_id'])
            groupJSON = StudyGroupSerilizer(group).data
            print(groupJSON)
            queryset[groupJSON['studygroup_id']] = groupJSON

        return Response(queryset)
        
class GetAllStudyGroups(APIView):
    """
    @ function
        Allows a user to request for all avalible study groups
    @ request Params
        none
    @ Return 
        queryset that contains study groups along with their information
    """
    def get(self, request, *args, **kwargs):
        queryset = {}
        if StudyGroup.objects.all() == []:
            return Response({
                "Message": "No availible study gorups"
            })
        for group in StudyGroup.objects.all():
            groupJSON = StudyGroupSerilizer(group).data
            queryset[groupJSON['studygroup_id']] = groupJSON

        return Response(queryset)

    
class CreateStudyGroup(ObtainAuthToken):
    """
    @ function
        Allows a user to create a new study group
            Doing so will create the following
                - Chatroom for study group
                - Study Enroll (Link between account and study group)
    @ request Params
        user token: request.data['token']
        studygroup name: request.data['studygroup_name']
        invite only: request.data['invite_only'] - only avalible for invited users
        //Add study group description later on
    @ Return 
        Error:
            study group name is already taken

        queryset that contains all enrolled study groups along with their information
    """
    def post(self, request, *args, **kwargs):

        def createStudyGroupChat(host):
            chat_toCreate = ChatRoom.objects.create(
                chatroom_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                chatroom_host = host
            )
            chat_toCreate.save()
            return chat_toCreate

        def StudyGroupNameCheck(name):
            try: 
                query = StudyGroup.objects.get(studygroup_name=name)
                return True
            except StudyGroup.DoesNotExist:
                return False

        def createStudyGroupEnroll(StudyGroupChat_toCreate, currentUser):
            StudyEnroll_toCreate = StudyEnroll.objects.create(
                studygroup_id = StudyGroupChat_toCreate,
                account = currentUser,
            )
            StudyEnroll_toCreate.save()

            return StudyEnroll_toCreate

        #Get current user
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        #Check name
        if StudyGroupNameCheck(request.data['name']):
            return Response({
                "Message": "Study group name already taken"
            })

        StudyGroupChat_toCreate = createStudyGroupChat(currentUser)
        StudyGroup_toCreate = StudyGroup.objects.create(
            #Add field for a study group name
            studygroup_name = request.data['name'],
            studygroup_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            invite_only = request.data['invite_only'],
            studygroup_host = currentUser,
            chat_id = StudyGroupChat_toCreate,
        )

        StudyGroup_toCreate.save()
        
        StudyGroupEnroll_toCreate = createStudyGroupEnroll(StudyGroup_toCreate, currentUser)

        return Response(StudyGroupSerilizer(StudyGroup_toCreate).data)

class JoinStudyGroup(ObtainAuthToken):
    """
    @ function
        Given a list of joinable studygroups a user has the ability to join a studygroup
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id'](The Key for the group)
    @ Return    
        Fail:
            Account is already in the study group
        Success:
            Account successfully join study group
    """
    def post(self, request, *args, **kwargs):
        print(request.data['studygroup_id'])
        def StudyEnrollCheck(studygroup, currentUser):
            #Do more chekcing
            try:
                studygroup_toEnroll = StudyEnroll.objects.all().get(studygroup_id=studygroup, account=currentUser)
                return({
                    "Message": "Account is already enrolled in this study group"
                })
            except StudyEnroll.DoesNotExist:
                studygroup_toEnroll = StudyEnroll.objects.create(
                    studygroup_id = studygroup,
                    account = currentUser,
                )
                studygroup_toEnroll.save()

            return({
                "Message": "Study group joined"
            })

        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        print(studygroup)
        StudyGroupEnroll_message = StudyEnrollCheck(studygroup, currentUser)


        return Response(StudyGroupEnroll_message)

class DeleteStudyGroup():
    pass
