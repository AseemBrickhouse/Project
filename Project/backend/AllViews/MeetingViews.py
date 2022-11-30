from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime, timedelta, time
import random
import string

DATE_FORMAT_FULL = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT_DATE = "%Y-%m-%d"
DATE_FORMAT_TIME = "%H:%M"

class CreateMeeting(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        def CheckMeetingTimes(meetings, to_add_start, to_add_end):
            today = datetime.now().strftime(DATE_FORMAT_FULL)
            format_date_today = datetime.strptime(today, DATE_FORMAT_FULL)
            #loop through each entry, if such meeting exists that overlaps with the one to create, then return
            for meeting in meetings:
                meeting_end = meeting.end_time.strftime(DATE_FORMAT_FULL)
                meeting_start = meeting.start_time.strftime(DATE_FORMAT_FULL)
                format_meeting_start = datetime.strptime(meeting_start, DATE_FORMAT_FULL)
                format_meeting_end = datetime.strptime(meeting_end, DATE_FORMAT_FULL)
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
        start_time = datetime.strptime(request.data['start_time'], DATE_FORMAT_FULL)
        end_time = datetime.strptime(request.data['end_time'], DATE_FORMAT_FULL)



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
            meeting_json = MeetingSerializer(meeting).data
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
        
        def GetTimeSlots(account_meetings, query_date):
            start_end = [u'08:00', u'17:00']
            time_slots = {}
            queryset = {}
            start_end_convert = sorted(datetime.strptime(x, '%H:%M') for x in start_end)
            res = [ (time(t,0,0,0).strftime("%H:%M"), time(t,30,0,0).strftime("%H:%M")) for t in range(min(start_end_convert).hour, max(start_end_convert).hour)]
            res += [ (time(t,30,0,0).strftime("%H:%M"), time(t+1,0,0,0).strftime("%H:%M")) for t in range(min(start_end_convert).hour, max(start_end_convert).hour)]

            for meeting in account_meetings:
                meeting_end = meeting.end_time.strftime(DATE_FORMAT_FULL)
                meeting_start = meeting.start_time.strftime(DATE_FORMAT_FULL)
                format_meeting_start = datetime.strptime(meeting_start, DATE_FORMAT_FULL)
                format_meeting_end = datetime.strptime(meeting_end, DATE_FORMAT_FULL)

                meeting_date = meeting.start_time.strftime(DATE_FORMAT_DATE)
                format_meeting_date = datetime.strptime(meeting_date, DATE_FORMAT_DATE)

                if format_meeting_date == query_date:    
                    queryset[meeting.meeting_code] = {
                        "start_time" : format_meeting_start,
                        "end_time" : format_meeting_end
                    }
            
            start_index = 0
            i = 0
            res = sorted(res)
            print(res)
            for key in sorted(queryset):
                start = queryset[key]['start_time'].strftime(DATE_FORMAT_TIME)
                end = queryset[key]['end_time'].strftime(DATE_FORMAT_TIME)
                index = res.index((start, end))
                for x in range(start_index, index):
                    time_slots[i] = {
                            "start_time": res[x][0],
                            "end_time": res[x][1]
                            }
                    i += 1
                time_slots[i] = {
                            "start_time": "Taken",
                            "end_time": "Taken"
                            }
                i += 1
                start_index = index + 1
            for x in range(start_index, len(res)):
                print(x, start_index, len(res))
                print(x, res[x])
                time_slots[i] = {
                    "start_time": res[x][0],
                    "end_time": res[x][1]
                }
                i+= 1
            
            return time_slots


        format_query_date = datetime.strptime(request.data['date'], "%Y-%m-%d")
        try:
            account = Account.objects.all().get(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
            )
            account_meetings = Meeting.objects.all().filter(user1=account) | Meeting.objects.all().filter(user2=account)
            queryset = GetTimeSlots(account_meetings, format_query_date)
            
            return Response(queryset)
        
        except Account.DoesNotExist:
            return Response({
                "Message": "User to get is not a valid user."
            })