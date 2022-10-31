from rest_framework import viewsets
from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime


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
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0].account

        try:
            #Need to check for both where user1=current_user  and user2=current_user
            #Need a way of formatting date (IDK how the dates are being past in from the frontend)
            pass
        except Meeting.DoesNotExist:
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
