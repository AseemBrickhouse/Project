from rest_framework import viewsets
from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime
import random
import string

def CheckMeeting(meeting_obj):
    today = datetime.now()
    format_date_today = today.strftime("%Y-%m-%d %H:%M:%S")

    format_end_time = meeting_obj.end_time.strftime("%Y-%m-%d %H:%M:%S")

    if format_end_time < format_date_today:
        meeting_obj.delete()
        return Response({
            "Meeting": "Meeting end time expired"
        })
    else:
        return

class CreateMeeting(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        def CheckMeetingTimes(meetings):
            #loop through each entry, if such meeting exists that overlaps with the one to create, then return
            for meeting in meetings:
                meeting_json = MeetingSerilizer(meeting).data
                meeting_start_time = meeting.start_time.strftime("%Y-%m-%d %H:%M:%S")
                meeting_end_time = meeting.end_time.strftime("%Y-%m-%d %H:%M:%S")

                # if the meeting to create start time falls inbetween a current users meeting start and end then return (can't create)
            return False
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0].account

        recipiet = None

        try:
            recipiet = Account.objects.all().get(
                email = request.data['email']
            )   
        except Account.DoesNotExist:
            return Response({
                "Message": "This user does not exists"
            })

        #Get all the the current user meetings at that time
        all_meetings_user = Meeting.objects.all().filter(user1=current_user) | Meeting.objects.all().filter(user2=current_user)
        all_meetings_recipient = Meeting.objects.all().filter(user1=recipiet) | Meeting.objects.all().filter(user2=recipiet)
        
        if CheckMeetingTimes(all_meetings_user) or CheckMeetingTimes(all_meetings_recipient):
            return Response({
                "Message" : "You are the recipient currently has a meeting at this time"
            })

        
        #Only do this is all checks pass i.e no meeting at that time
        try:
            #Need to check for both where user1=current_user  and user2=current_user
            #Need a way of formatting date (IDK how the dates are being past in from the frontend)
            pass
        except Meeting.DoesNotExist:
            meeting_to_create = Meeting.objects.create(
                meeting_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                topic = request.data['topic'],
                user1 = current_user,
                user2 = recipiet,

            )
            pass

class GetUserMeetings(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0].account

        all_meetings = Meeting.objects.all().filter(user1=current_user) | Meeting.objects.all().filter(user2=current_user)

        queryset = {}
        for meeting in all_meetings:
            meeting_json = MeetingSerilizer(meeting).data
            queryset[meeting_json['meeting_code']] = meeting_json

        return Response(queryset)

class DeleteMeeting(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0].account

        #Note:
        #It something werid happens then we will need to check user1 and user2
        #We should not need to do this if we only show the right meetings on the front end
        try:
            meeting_to_delete = Meeting.objects.all().get(meeting_id=request.data['meeting_code'])
            meeting_to_delete.delete()
        except Meeting.DoesNotExist:
            return Response({
                "Message": "Meeting does not exists"
            })
