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
    def post(self, request, *args, **kwargs):
        pass

class DeleteAnnouncement(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        pass

class UpdateAnnouncement(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        message  = request.data['announcement_description']
        announcement = announcement.objects.all().get(announcement_id=request.data['announcement_id'])
        if not message:
            return Response({
                "Message": "No changes made."
            })
        else:
            announcement.announcement_description = message
            announcement.save(update_fields=['announcement_description'])
            return Response({
                "Message": "Announcement description succesfully changes"
            })

class GetGroupAnnouncements(APIView):
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