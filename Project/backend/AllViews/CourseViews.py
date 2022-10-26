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

class GetAllCourses(APIView):
    def get(self, request, *args, **kwargs):

        queryset = {}

        for course in Course.objects.all():
            courseJSON = CourseSerilizer(course).data
            queryset[courseJSON['course_id']] = courseJSON

        return Response(queryset)

class GetUsersInCourse(APIView):
    def post(self, request, *args, **kwargs):

        course = Course.objects.all().get(course_id=request.data['couse_id'])

        queryset = {}

        for enroll in CourseEnroll.objects.all().filter(course=course):
            user = enroll.account
            user_json = AccountSerilizer(user).data
            queryset[user_json['key']] = user_json

        return Response(queryset)
        
class CreateCourse(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        #Check if course exits if not create it
        #Duplicate course codes do not matter because different people can make diff courses
        #edge cases: ?

        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account
        course_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

        # professor-> ?
        # ta-> ?
    
        try:
            Course.objects.all().get(
                course_owner=current_user,
                course_name=request.data['course_name'],
                course_code=request.data['course_code'],
                course_description=request.data['course_description'],
            )
        except Course.DoesNotExist:
            course_to_create = Course.objects.create(
                course_owner=current_user,
                course_name=request.data['course_name'],
                course_code=request.data['course_code'],
                course_description=request.data['course_description'],
            )
            course_to_create.save()
    
        return Response({
            "Message": "Course successfully created"
        })

#
#class CourseModlue(APIView):
#   Create a new model
#
#
