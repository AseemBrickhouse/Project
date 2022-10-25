from wsgiref.handlers import format_date_time
from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime
from django.utils import timezone
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

        if not StudyGroup.objects.all():
            return Response({
                "Message": "You are not in any study groups currently"
        })

        for enroll in StudyEnroll.objects.all().filter(account=currentUser):
            studygroup = enroll.studygroup_id
            groupJSON = StudyGroupSerilizer(studygroup).data
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
            studygroup_name = request.data['name'],
            studygroup_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            invite_only = request.data['invite_only'],
            studygroup_host = currentUser,
            chat_id = StudyGroupChat_toCreate,
        )

        StudyGroup_toCreate.save()
        
        StudyGroupEnroll_toCreate = createStudyGroupEnroll(StudyGroup_toCreate, currentUser)
        StudyGroup_toCreateJSON = StudyGroupSerilizer(StudyGroup_toCreate).data
        
        return Response(StudyGroup_toCreateJSON)

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
        #Implement functionality later on to have more people to create invites and not just the host
        def StudyEnrollCheck(studygroup, currentUser):
            #Do more chekcing
            studygroupJSON = StudyGroupSerilizer(studygroup).data
            try:
                studygroup_toEnroll = StudyEnroll.objects.all().get(studygroup_id=studygroup, account=currentUser)
                return({
                    "Message": "Account is already enrolled in this study group"
                })
            except StudyEnroll.DoesNotExist:
                if studygroupJSON['invite_only']:
                    #check if invite exist
                    #need to check exipriation date
                    today = datetime.now()
                    #Get invite if it exist
                    hasInvite = Invite.objects.all().filter(
                            sender=studygroupJSON['studygroup_host'], 
                            recipient=currentUser,
                            studygroup_id=studygroup,
                        )
                    if not hasInvite:
                        return ({
                             "Message": "You do not have a invite to this group!"
                         })
                    else:
                        #At this point the invite must exist at [0]
                        hasInvite = hasInvite[0]
                        #Format both of the dates to be compared
                        format_date_today = today.strftime("%Y-%m-%d %H:%M:%S")
                        format_date_exp = hasInvite.expiration_date.strftime("%Y-%m-%d %H:%M:%S")
                        
                        #If the exp is lower -> the invite is expired
                        #So, do not join the group and delete the invite
                        if format_date_exp < format_date_today:
                            hasInvite.delete()
                            return ({
                                "Message": "Invite expired!"
                            })

                #After all checks are passed its safe to enroll the user in the group
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

        StudyGroupEnroll_message = StudyEnrollCheck(studygroup, currentUser)


        return Response(StudyGroupEnroll_message)


class GetUserHostedGroups(ObtainAuthToken):
    """
    @ function
        Given a user token, return all study groups hosted by the current user
    @ request Params
        user token: request.data['token']
    @ Return    
        All groups that are hosted by the user
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        allUserHostedGroups = StudyGroup.objects.all().filter(studygroup_host=currentUser)

        if not allUserHostedGroups:
            return Response({
                "Message": "No hosted groups"
            })

        queryset = {}

        for group in allUserHostedGroups:
            groupJSON = StudyGroupSerilizer(group).data
            queryset[groupJSON['studygroup_id']] = groupJSON

        return Response(queryset)

class DeleteStudyGroup(ObtainAuthToken):
    """
    @ function
        Given a user token, delete one of the hosted groups
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id']
    @ Return    
        message telling whether or not the group was deleted
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        key = request.data['studygroup_id']

        try:
            toDelete = StudyGroup.objects.get(studygroup_host=currentUser, studygroup_id=key)
            
            #Deleting the chat room deletes all the enrolls, group, and the chatroom
            toDelete.chat_id.delete()

            return Response({
                "Message": "Study group successfully deleted"
            })

        except StudyGroup.DoesNotExist:
            #Shouldn't ever get here if we error check and display the right information on the frontend
            return Response({
                "Message": "You are not the host of this group"
            })

class GetUsersInGroup(APIView):
    """
    @ function
        Given a studygroup_id return all users in that group
    @ request Params
        studygroup id: request.data['studygroup_id']
    @ Return    
        A list of current enrolled users in that group
    """
    def post(self, request, *args, **kwargs):
        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])

        userList = StudyEnroll.objects.all().filter(studygroup_id=studygroup)

        queryset = {}

        for user in userList:
            userJSON = AccountSerilizer(user.account).data
            queryset[userJSON['key']] = userJSON

        return Response(queryset)


class LeaveStudyGroup(ObtainAuthToken):
    """
    @ function
        Given a user token and a studygroup_id, leave one of the user study groups
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id']
    @ Return    
        Message telling whether or not the user has left the group
    """
    def post(self, request, *args, **kwargs):
        #   More checks to be done
        #   When the last user of the group leaves -> delete the group
        #   Who gets host when the host leaves -> the next person in-line of study enroll
        
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])  
        studygroup_userlist = StudyEnroll.objects.all().filter(studygroup_id=studygroup)

        #Special case when current user is the host i.e cant host a group youre not in :)
        if currentUser == studygroup.studygroup_host:
            #More than 1 person in group so delegate host
            if len(studygroup_userlist) > 1:
                studygroup.studygroup_host = studygroup_userlist[1].account
                studygroup.save(update_fields=['studygroup_host'])  
                               
            else:
                #Safe to delete study group if the last person in the group leaves
                studygroup.delete()
                return Response({
                    "Message": "Group successfully left and group is deleted(No more active users)."
                })
        
        try:
            #Remove the user from the group if they exist
            toLeave = StudyEnroll.objects.all().get(studygroup_id=studygroup, account=currentUser)
            toLeave.delete()

            return Response({
                "Message": "You have successfully left the group"
            })
        except StudyEnroll.DoesNotExist:
            return Response({
                "Message": "You are not in this study group"
            })

class GetGroupModules(APIView):
    """
    @ function
        Given a studygroup_id, return all Modules in a study group along with their content
    @ request Params
        studygroup id: request.data['studygroup_id']
    @ Return    
        A list of Modules that are reltated to the current study group and their content
    """
    def post(self, request, *args, **kwargs):
        def getContent(module):
            queryset = {}

            for entry in  Material.objects.all().filter(module_id=module):
                entryJSON = MaterialSerlizer(entry).data
                queryset[entryJSON['material_id']] = entryJSON

            return queryset

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        studygroupJSON = StudyGroupSerilizer(studygroup).data

        studygroup_modules = Module.objects.all().filter(studygroup_id=studygroupJSON['id'])

        queryset = {}

        for module in studygroup_modules:
            moduleJSON = ModuleSerilizer(module).data
            queryset[moduleJSON['module_id']] = moduleJSON
            queryset[moduleJSON['module_id']]['content'] = getContent(module)

        return Response(queryset)