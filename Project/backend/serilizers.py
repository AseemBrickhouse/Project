from rest_framework import serializers
from .models import *

class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields=(
            'user',
            'creation_date',
            'key',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'bio',
            # SEE MODELS COMMENT
            # 'profile_pic',
        )

class FriendsSerilize(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = (
            'user1',
            'user2',
            'creation_date'
        )

class MeetingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = (
            'meeting_code',
            'creation_date',
            'topic',
            'start_time',
            'end_time',
            'user1',
            'user2',
        )

class CourseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'course_id',
            'creation_date',
            'professor',
            'ta',
            'course_name',
            'course_code',
            'course_description',
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
        model = Message
        fields = (
            'message_id',
            'chatroom_id',
            'creation_date',
            'account',
            'content',
        )

class ChatRoomSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = (
            'chatroom_id',
            'chatroom_host',
        )

class ModuleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = (
            'id',
            'module_id',
            'creation_date',
            'studygroup_id',
        )

class Announcements(serializers.ModelField):
    class Meta:
        model = Announcements
        fields = (
            'announcements_id',
            'creation_date',
            'studygroup_id'
        )

class StudyGroupSerilizer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ( 
            'id',
            'studygroup_id',
            'creation_date',
            'studygroup_name',
            'studygroup_host',
            'chat_id',
            'invite_only',
        )

class StudyEnrollSelizer(serializers.ModelSerializer):
    class Meta:
        model = StudyEnroll
        fields = (
            'account',
            'studygroup_id'
        )

class MaterialSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'material_id',
            'material_type',
            'creation_date',
            'account',
            'module_id',
            'content',
            'file_content',
        )

class InviteSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = (
            'id',
            'sender',
            'creation_date',
            'expiration_date',
            'recipient',
            'studygroup_id',
        )