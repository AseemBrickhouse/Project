from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime
import random
import string

class CreateAnnouncement(ObtainAuthToken):
    """
    @ function
        Given a user token, studygroup_id, and an announcement_description, create an announcement for the current group
    @ request Params
        user token: request.data['token']
        studygroup id: request.data['studygroup_id']
        announcement description: request.data['announcement_description']
    @ Return    
        Message telling whether or not the announcement was created
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])

        if studygroup.studygroup_host != current_user:
            return Response({
                "Message": "Only the study group host can create announcements."
            })

        try:
            announcement = Announcements.objects.all().get(
                announcement_description = request.data['announcement_description']
            )
            return Response({
                "Message": "Announcement already exists"
            })

        except Announcements.DoesNotExist:
            announcement = Announcements.objects.create(
                announcement_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                studygroup_id = studygroup,
                announcement_creator = current_user,
                announcement_description = request.data['announcement_description'],
            )
            announcement.save()

        return Response({
            "Message": "Announcement succesfully create"
        })

class DeleteAnnouncement(ObtainAuthToken):
    """
    @ function
        Given a user token, and an announcement_id, delete the announcement from the group
    @ request Params
        user token: request.data['token']
        announcement id: request.data['announcement_id']
    @ Return    
        Message telling whether or not the announcement was deleted
    """
    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        if not request.data.__contains__('announcement_id'):
            return Response({
                "Message": "No given announcement id"
            })
                
        announcement = Announcements.objects.all().filter(announcement_id=request.data['announcement_id'])

        if not announcement:
            return Response({
                "Message" : "Announcement does not exists"
            })
        else:
            if announcement[0].announcement_creator != current_user:
                return Response({
                    "Message": "You are not the creator of this announcement"
                })
            else:
                announcement[0].delete()

                return Response({
                    "Message": "Announcement succesfully deleted"
                })

class UpdateAnnouncement(ObtainAuthToken):
    """
    @ function
        Given a user token, and an announcement_id, update the announcement for the current group
    @ request Params
        user token: request.data['token']
        announcement id: request.data['announcement_id']
    @ Return    
        Message telling whether or not the announcement was updated
    """
    def put(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        message  = request.data['announcement_description']
        announcement = Announcements.objects.all().get(announcement_id=request.data['announcement_id'])
        if announcement.announcement_creator != current_user:
            return Response({
                "Message": "You are not the study group host"
            })
        if not message:
            return Response({
                "Message": "No changes made."
            })
        else:
            announcement.announcement_description = message
            announcement.save(update_fields=['announcement_description'])
            return Response({
                "Message": "Announcement description succesfully changed"
            })

class GetGroupAnnouncements(APIView):
    """
    @ function
        Retrive all announcements of a study group
    @ request Params
       studygroup id: request.data['studygroup_id']
    @ Return    
        All announncements and their data in json format
    """
    def post(self, request, *args, **kwargs):
        queryset = {}

        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])

        studygroup_announcements = Announcements.objects.all().filter(studygroup_id=studygroup)

        for announcement in studygroup_announcements:
            announcement_json = AnnouncementSerilizer(announcement).data
            queryset[announcement_json['announcement_id']] = announcement_json
            queryset[announcement_json['announcement_id']]['studygroup_id'] = StudyGroupSerilizer(studygroup).data

            announcement_creator = Account.objects.all().get(key=announcement.announcement_creator.key)
            announcement_creator_json = AccountSerilizer(announcement_creator).data
            queryset[announcement_json['announcement_id']]['announcement_creator'] = announcement_creator_json

        return Response(queryset)

class EnrolledGroupAnnouncements(ObtainAuthToken):
    """
    @ function
        Retrive all announcements of enrolled study group
    @ request Params
        user token: request.data['token']
    @ Return    
        All studygroup and their announncements along with their data
    """
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        study_enroll = StudyEnroll.objects.all().filter(account=current_user)

        queryset = {}

        for enroll in study_enroll:
            studygroup = StudyGroup.objects.all().get(studygroup_id=enroll.studygroup_id.studygroup_id)
            studygroup_json = StudyGroupSerilizer(studygroup).data
            
            studygroup_announcements = Announcements.objects.all().filter(studygroup_id=studygroup)

            queryset[studygroup_json['studygroup_id']] = {}       

            if studygroup_announcements:
                for announcement in studygroup_announcements:
                    announcement_json = AnnouncementSerilizer(announcement).data
                    queryset[studygroup_json['studygroup_id']][announcement_json['announcement_id']] = announcement_json

                    queryset[studygroup_json['studygroup_id']][announcement_json['announcement_id']]['studygroup_id'] = studygroup_json

                    announcement_creator = Account.objects.all().get(key=announcement.announcement_creator.key)
                    announcement_creator_json = AccountSerilizer(announcement_creator).data
                    queryset[studygroup_json['studygroup_id']][announcement_json['announcement_id']]['announcement_creator'] = announcement_creator_json

        return Response(queryset)