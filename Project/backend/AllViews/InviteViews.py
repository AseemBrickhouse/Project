from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime
import random
import string


def CheckTimes(invite):
    today = datetime.now()
    format_date_today = today.strftime("%Y-%m-%d %H:%M:%S")
    format_date_exp = invite.expiration_date.strftime("%Y-%m-%d %H:%M:%S")

    #Create new invite with updated date
    if format_date_exp < format_date_today:
        pass
    pass

class CreateInvite(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        #only host can create invites rn
        
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        recipient = Account.objects.all().get(key=request.data['key'])
        if not recipient:
            return Response({
                "Message": "Person to invite does not exist"
            })

        studygroup = StudyGroup.objects.all().filter(studygroup_id=request.data['studygroup_id'])
        if not studygroup:
            return Response({
                "Message": "Studygroup does not exists"
            })
        
        is_enrolled = StudyEnroll.objects.all().filter(studygroup_id=studygroup[0], account=recipient)
        if is_enrolled:
            return Response({
                "Message": recipient.first_name + " " + recipient.last_name + " is already enrolled in " + studygroup[0].studygroup_name
            })

        if studygroup[0].studygroup_host == current_user:
            try:
                invite = Invite.objects.all().get(
                    sender=current_user,
                    recipient = recipient,
                    studygroup_id=studygroup[0],
                )
                
                #then check time
                # CheckTimes(invite)
                return Response({
                    "Message": "Outbound invite already exists"
                })
            except Invite.DoesNotExist:
                #Check to see if exp date is greate than today if not -> Error
                invite = Invite.objects.create(
                    invite_id=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                    sender=current_user,
                    recipient = recipient,
                    studygroup_id=studygroup[0],
                    #somehow put dates in
                )
                print("get")
                invite.save()

            return Response({
                "Message": recipient.first_name + " " + recipient.last_name + " has been invited to " + studygroup[0].studygroup_name
            })
        else:
            return Response({
                "Message": "You are not the host of this group"
            })


class DeleteInvite(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        if not request.data.__contains__('invite_id'):
            return Response({
                "Message": "No given invite id"
            })

        invite = Invite.objects.all().filter(invite_id=request.data['invite_id'])

        if not invite:
            return Response({
                "Message": "Not a valid invite to delete"
            })
        else:
            if invite[0].sender != current_user:
                return Response({
                    "Message": "You are not the sender of this invite"
                })
             
            invite[0].delete()

            return Response({
                "Message": "Invite successfully deleted"
            })
    

class GetOutboundInvites(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        outbound_invites = Invite.objects.all().filter(sender=current_user)
        queryset = {}
        if not outbound_invites:
            return Response({
                "Message": "No current sent invites"
            })
        for invite in outbound_invites:
            invite_json = InviteSerlizer(invite).data
            queryset[invite_json['invite_id']] = invite_json

            sender =  Account.objects.all().get(id=invite_json['sender'])
            sender_json = AccountSerilizer(sender).data
            queryset[invite_json['invite_id']]['sender'] = sender_json

            recipient_json = AccountSerilizer(current_user).data
            queryset[invite_json['invite_id']]['recipient'] = recipient_json
            
            studygroup = StudyGroup.objects.all().get(id=invite_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data
            queryset[invite_json['invite_id']]['studygroup_info'] = studygroup_json
        
        return Response(queryset)

class GetInboundInvites(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        inbound_invites = Invite.objects.all().filter(recipient=current_user)
        queryset = {}
        if not inbound_invites:
            return Response({
                "Message": "No current invites"
            })

        for invite in inbound_invites:
            invite_json = InviteSerlizer(invite).data
            queryset[invite_json['invite_id']] = invite_json

            sender =  Account.objects.all().get(id=invite_json['sender'])
            sender_json = AccountSerilizer(sender).data
            queryset[invite_json['invite_id']]['sender'] = sender_json

            recipient_json = AccountSerilizer(current_user).data
            queryset[invite_json['invite_id']]['recipient'] = recipient_json
            
            studygroup = StudyGroup.objects.all().get(id=invite_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data
            queryset[invite_json['invite_id']]['studygroup_info'] = studygroup_json
        
        return Response(queryset)

class GetGroupInvites(APIView):
    def post(self, request, *args, **kwargs):
        #Do I need an Account???? not sure

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        group_invites = Invite.objects.all().filter(studygroup_id=studygroup)
        
        queryset = {}

        if not group_invites:
            return Response({
                "Message": "No current outgoing group invites"
            })
        
        for invite in group_invites:
            invite_json = InviteSerlizer(invite).data
            queryset[invite_json['invite_id']] = invite_json

            sender =  Account.objects.all().get(id=invite_json['sender'])
            sender_json = AccountSerilizer(sender).data
            queryset[invite_json['invite_id']]['sender'] = sender_json

            recipient = Account.objects.all().get(id=invite_json['recipient'])
            recipient_json = AccountSerilizer(recipient).data
            queryset[invite_json['invite_id']]['recipient'] = recipient_json
            
            studygroup = StudyGroup.objects.all().get(id=invite_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data
            queryset[invite_json['invite_id']]['studygroup_info'] = studygroup_json
        
        return Response(queryset)