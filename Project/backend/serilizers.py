from dataclasses import field
from rest_framework import serializers
from .models import *

class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields=(
            'user',
            'key',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
        )

class MeetingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = (
            'meeting_code',
            'user1',
            'user2',
        )

class CourseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'course_id',
            'professor',
            'ta',
            'course_name',
            'course_code',
        )

class CourseEnrollSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnroll
        fields = (
            'account',
            'course',
        )

class MessageSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'message_id',
            'account',
            'content',
        )

class ChatRoomSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'chatroom_id',
            'chatroom_host',
            'messages',
        )
    
class StudyGroupSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = ( 
            'studygroup_id',
            'stduygroup_host',
            'chat_id'
        )

class StudyEnrollSelizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'material_id',
            'account',
            'studygroup_id'
            'content'
        )