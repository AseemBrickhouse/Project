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

class GetStudyGroup(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        try:
            studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        except StudyGroup.DoesNotExist:
            return Response({
                "Message": "Error"
            })
        queryset = StudyGroupSerializer(studygroup).data
        is_enrolled = StudyEnroll.objects.all().filter(studygroup_id=studygroup.id, account=current_user)
        queryset['is_enrolled'] = False if not is_enrolled else True

        return Response(queryset)

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
        current_user = User.objects.all().filter(id=token)[0].account

        queryset = {}

        if not StudyGroup.objects.all():
            return Response({
                "Message": "You are not in any study groups currently"
        })

        for enroll in StudyEnroll.objects.all().filter(account=current_user):
            studygroup = enroll.studygroup_id
            group_json = StudyGroupSerializer(studygroup).data
            queryset[group_json['studygroup_id']] = group_json
            # is_enrolled = StudyEnroll.objects.filter(account = current_user, studygroup=)
            queryset[group_json['studygroup_id']]['is_enrolled'] = True

            host = Account.objects.all().get(id=group_json['studygroup_host'])
            host_json = AccountSerializer(host).data
            queryset[group_json['studygroup_id']]['studygroup_host'] = host_json

            queryset[group_json['studygroup_id']]['invites_out'] = len(Invite.objects.all().filter(studygroup_id=group_json['id']))
        return Response(queryset)
        
class GetAllStudyGroups(ObtainAuthToken):
    """
    @ function
        Allows a user to request for all avalible study groups
    @ request Params
        none
    @ Return 
        queryset that contains study groups along with their information
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        queryset = {}
        if StudyGroup.objects.all() == []:
            return Response({
                "Message": "No availible study gorups"
            })
        for group in StudyGroup.objects.all():
            group_json= StudyGroupSerializer(group).data
            queryset[group_json['studygroup_id']] = group_json
            is_enrolled = StudyEnroll.objects.all().filter(account=current_user, studygroup_id=group)
            queryset[group_json['studygroup_id']]['is_enrolled'] = False if not is_enrolled else True

            host = Account.objects.all().get(id=group_json['studygroup_host'])
            host_json = AccountSerializer(host).data
            queryset[group_json['studygroup_id']]['studygroup_host'] = host_json

            queryset[group_json['studygroup_id']]['invites_out'] = len(Invite.objects.all().filter(studygroup_id=group_json['id']))

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
        studygroup description: request.data['studygroup_description'] ccan be null
    @ Return 
        Error:
            study group name is already taken

        queryset that contains all enrolled study groups along with their information
    """
    def post(self, request, *args, **kwargs):

        def StudyGroupNameCheck(name):
            if not name:
                return True
            try: 
                StudyGroup.objects.get(studygroup_name=name)
                return True
            except StudyGroup.DoesNotExist:
                return False

        def createStudyGroupChat(host):
            chat_to_create = ChatRoom.objects.create(
                chatroom_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                chatroom_host = host
            )
            chat_to_create.save()
            return chat_to_create

        def createStudyGroupEnroll(StudyGroup_to_create, current_user):
            StudyEnroll_to_create = StudyEnroll.objects.create(
                studygroup_id = StudyGroup_to_create,
                account = current_user,
            )
            StudyEnroll_to_create.save()

            return StudyEnroll_to_create


        
        #Get current user
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        #Check name
        if StudyGroupNameCheck(request.data['studygroup_name']):
            return Response({
                "Message": "Study group name already taken"
            })

        StudyGroup_chat_to_create = createStudyGroupChat(current_user)

        studygroup_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

        StudyGroup_to_create = StudyGroup.objects.create(
            studygroup_name = request.data['studygroup_name'],
            studygroup_id = studygroup_id,
            invite_only = request.data['invite_only'],
            studygroup_host = current_user,
            chat_id = StudyGroup_chat_to_create,
            studygroup_description = request.data['studygroup_description'] if request.data['studygroup_description'] != '' else None
        )

        StudyGroup_to_create.save()
        
        createStudyGroupEnroll(StudyGroup_to_create, current_user)

        StudyGroup_to_create_json = StudyGroupSerializer(StudyGroup_to_create).data

        studygroup_host_name = current_user.first_name + " " + current_user.last_name

        #Create file
        init(studygroup_id, studygroup_host_name, StudyGroup_chat_to_create.chatroom_id)
 
        return Response({
            "Message" : "Group succesfully created"
        })

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
        def StudyEnrollCheck(studygroup, current_user):
            #Do more chekcing
            studygroup_json = StudyGroupSerializer(studygroup).data
            try:
                studygroup_to_enroll = StudyEnroll.objects.all().get(studygroup_id=studygroup, account=current_user)
                return({
                    "Message": "Account is already enrolled in this study group"
                })
            except StudyEnroll.DoesNotExist:
                if studygroup_json['invite_only']:
                    #check if invite exist
                    #need to check exipriation date
                    today = datetime.now()
                    #Get invite if it exist
                    has_invite = Invite.objects.all().filter(
                            sender=studygroup_json['studygroup_host'], 
                            recipient=current_user,
                            studygroup_id=studygroup,
                        )
                    if not has_invite:
                        return ({
                             "Message": "You do not have a invite to this group!"
                         })
                    else:
                        #At this point the invite must exist at [0]
                        has_invite = has_invite[0]
                        if has_invite.expiration_date != None:
                            #Format both of the dates to be compared
                            format_date_today = today.strftime("%Y-%m-%d %H:%M:%S")
                            format_date_exp = has_invite.expiration_date.strftime("%Y-%m-%d %H:%M:%S")

                            #If the exp is lower -> the invite is expired
                            #So, do not join the group and delete the invite
                            if format_date_exp < format_date_today:
                                has_invite.delete()
                                return ({
                                    "Message": "Invite expired!"
                                })

                            has_invite.delete()
                #After all checks are passed its safe to enroll the user in the group
                studygroup_to_enroll = StudyEnroll.objects.create(
                    studygroup_id = studygroup,
                    account = current_user,
                )
                studygroup_to_enroll.save()

            return({
                "Message": "Study group joined"
            })

        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])

        StudyGroup_enroll_message = StudyEnrollCheck(studygroup, current_user)


        return Response(StudyGroup_enroll_message)


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
        current_user = User.objects.all().filter(id=token)[0].account

        all_user_hosted_groups = StudyGroup.objects.all().filter(studygroup_host=current_user)

        if not all_user_hosted_groups:
            return Response({
                "Message": "No hosted groups"
            })

        queryset = {}

        for group in all_user_hosted_groups:
            group_json = StudyGroupSerializer(group).data
            queryset[group_json['studygroup_id']] = group_json
            # is_enrolled = StudyEnroll.objects.all().filter(studygroup_id=studygroup.id, account=current_user)
            queryset[group_json['studygroup_id']]['is_enrolled'] = True

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
    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        key = request.data['studygroup_id']

        try:
            to_delete = StudyGroup.objects.get(studygroup_host=current_user, studygroup_id=key)
            
            #Deleting the chat room deletes all the enrolls, group, and the chatroom
            to_delete.chat_id.delete()

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

        user_list = StudyEnroll.objects.all().filter(studygroup_id=studygroup)

        queryset = {}

        for user in user_list:
            user_json = AccountSerializer(user.account).data
            queryset[user_json['key']] = user_json

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
    def delete(self, request, *args, **kwargs):
        #   More checks to be done
        #   When the last user of the group leaves -> delete the group
        #   Who gets host when the host leaves -> the next person in-line of study enroll
        
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        try:
            studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])  
        except StudyGroup.DoesNotExist:
            return Response({
                "Message": "Group does not exists"
            })
        studygroup_user_list = StudyEnroll.objects.all().filter(studygroup_id=studygroup)

        #Special case when current user is the host i.e cant host a group youre not in :)
        print(current_user, studygroup.studygroup_host)
        if current_user == studygroup.studygroup_host:
            #More than 1 person in group so delegate host
            if len(studygroup_user_list) > 1:
                studygroup.studygroup_host = studygroup_user_list[1].account
                studygroup.save(update_fields=['studygroup_host'])  
                               
            else:
                #Safe to delete study group if the last person in the group leaves
                studygroup.delete()
                return Response({
                    "Message": "Group successfully left and group is deleted(No more active users)."
                })
        
        try:
            #Remove the user from the group if they exist
            to_leave = StudyEnroll.objects.all().get(studygroup_id=studygroup, account=current_user)
            to_leave.delete()

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
                entry_json = MaterialSerlizer(entry).data
                queryset[entry_json['material_id']] = entry_json

                # account = Account.objects.get(id=entry_json['account'])
                # account_json = AccountSerializer(account).data
                # queryset[account_json['key']] = account_json

            return queryset

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        studygroup_json = StudyGroupSerializer(studygroup).data

        studygroup_modules = Module.objects.all().filter(studygroup_id=studygroup_json['id'])

        queryset = {}

        for module in studygroup_modules:
            module_json = ModuleSerializer(module).data
            queryset[module_json['module_id']] = module_json
            queryset[module_json['module_id']]['content'] = getContent(module)

            account = Account.objects.get(id=module_json['module_owner'])
            account_json = AccountSerializer(account).data
            queryset[module_json['module_id']]['module_owner'] = account_json
            
        return Response(queryset)