from rest_framework import viewsets
from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime
from datetime import date
from datetime import timedelta
import random
import string

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def CheckMeeting(all_meetings, to_add_start, to_add_end):
    today = datetime.now()
    format_date_today = today.strftime(DATE_FORMAT)

    for meeting in all_meetings:
        meeting_end = datetime.strftime(meeting.end_time, DATE_FORMAT)
        if meeting_end < format_date_today:
            meeting.delete()


    # format_end_time = meeting_obj.end_time.strftime(DATE_FORMAT)

    # if format_end_time < format_date_today:
    #     meeting_obj.delete()
    #     return Response({
    #         "Meeting": "Meeting end time expired"
    #     })
    # else:
    #     return

class CreateMeeting(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        def CheckMeetingTimes(meetings, to_add_start, to_add_end):
            today = datetime.now().strftime(DATE_FORMAT)
            format_date_today = datetime.strptime(today, DATE_FORMAT)
            #loop through each entry, if such meeting exists that overlaps with the one to create, then return
            for meeting in meetings:
                meeting_end = meeting.end_time.strftime(DATE_FORMAT)
                meeting_start = meeting.start_time.strftime(DATE_FORMAT)
                format_meeting_start = datetime.strptime(meeting_start, DATE_FORMAT)
                format_meeting_end = datetime.strptime(meeting_end, DATE_FORMAT)
                if format_meeting_end < format_date_today:
                      meeting.delete()
                else:
                    if format_meeting_start <= to_add_start <= format_meeting_end or format_meeting_start <= to_add_end <= format_meeting_end:
                        return False
                # if the meeting to create start time falls inbetween a current users meeting start and end then return (can't create)
            return True
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0].account

        recipiet = None

        try:
            recipiet = Account.objects.all().get(
                key = request.data['key']
            )   
        except Account.DoesNotExist:
            return Response({
                "Message": "This user does not exists"
            })

        #Get all the the current user meetings at that time
        start_time = datetime.strptime(request.data['start_time'], DATE_FORMAT)
        end_time = datetime.strptime(request.data['end_time'], DATE_FORMAT)



        all_meetings_user = Meeting.objects.all().filter(user1=current_user) | Meeting.objects.all().filter(user2=current_user)
        all_meetings_recipient = Meeting.objects.all().filter(user1=recipiet) | Meeting.objects.all().filter(user2=recipiet)

        if not CheckMeetingTimes(all_meetings_user,start_time, end_time) and not CheckMeetingTimes(all_meetings_recipient, start_time, end_time):
            return Response({
                "Message" : "You or the recipient currently has a meeting at this time"
            })
        
        #Only do this is all checks pass i.e no meeting at that time
        try:
            meeting_obj = Meeting.objects.get(
                user1=current_user,
                user2=recipiet,
                end_time=end_time,
                start_time=start_time,
            ) | Meeting.objects.get(
                user2=current_user,
                user1=recipiet,
                end_time=end_time,
                start_time=start_time,
            ) 
            return Response({
                "Message": "Meeting at current time already exists."
            })
            
        except Meeting.DoesNotExist:
            meeting_to_create = Meeting.objects.create(
                meeting_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                topic = request.data['topic'],
                user1 = current_user,
                user2 = recipiet,
                start_time=start_time,
                end_time=start_time + timedelta(minutes=30),
            )
            meeting_to_create.save()

            return Response({
                "Message": "Meeting successfully created."
            })
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
            if meeting_to_delete.user1 != current_user or meeting_to_delete.user2 != current_user:
                return Response({
                    "Message": "You are not in this meeting"
                })
            else:
                meeting_to_delete.delete()

                return Response({
                    "Message": "Meeting successfully deleted"
                })
        except Meeting.DoesNotExist:
            return Response({
                "Message": "Meeting does not exists"
            })

class GetOpenMeetingTimes(APIView):
    def post(self, request, *args, **kwargs):
        format_date = datetime.strptime(request.data['date'], "%Y-%m-%d")
        try:
            account = Account.objects.all().get(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
            )
            account_meetings = Meeting.objects.all().filter(user1=account) 
            account_meetings | Meeting.objects.all().filter(user2=account)
 
            var = {}
            for meeting in Meeting.objects.all().filter(user1=account) | Meeting.objects.all().filter(user2=account):
                print(meeting)
                meeting_end = meeting.end_time.strftime("%Y-%m-%d")
                meeting_start = meeting.start_time.strftime("%Y-%m-%d")
                format_meeting_start = datetime.strptime(meeting_start,"%Y-%m-%d")
                format_meeting_end = datetime.strptime(meeting_end, "%Y-%m-%d")
                var[meeting.meeting_code] = {
                    "start_time" : format_meeting_start,
                    "end_time" : format_meeting_end
                }
            #[<[9-9:30],[9:30-10:00]>]
                
                return Response(var)
        except Account.DoesNotExist:
            return Response({
                "Message": "User to get is not a valid user."
            })