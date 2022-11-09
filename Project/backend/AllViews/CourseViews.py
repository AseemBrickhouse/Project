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

class JoinCourse(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        course = None
        try:
            course = Course.objects.all().get(course_code=request.data['course_code'], course_id=request.data['course_id'])
        except Course.DoesNotExist:
            return Response({
                "Message": "Course to join does not exists"
            })

        course_enroll = CourseEnroll.objects.all().filter(account = current_user, course = course)

        if course_enroll:
            return Response({
                "Message": "You are already enrolled in this course."
            })
        else:
            course_to_join = CourseEnroll.objects.create(
                account = current_user,
                course = course
            )
            course_to_join.save()

        return Response({
            "Message": "You have succesfully joined the course."
        })

class LeaveCourse(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account

        course = Course.objects.all().get(course_id=request.data['course_id'])

        try:
            course_to_leave = CourseEnroll.objects.all().get(account=current_user, course=course)
            course_to_leave.delete()
            return Response({
                "Message": "You have succesfully left the course."
            })
        except CourseEnroll.DoesNotExist:
            return Response({
                "Message": "You are not enrolled in this course."
            })
            
class DeleteCourse(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        pass
#
#class CourseModlue(APIView):
#   Create a new model
#
#
