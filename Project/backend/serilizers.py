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
            'id',
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
            'id',
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
            'id',
            'account',
            'course',
        )

class MessageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
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

class AnnouncementSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = (
            'id',
            'announcement_id',
            'creation_date',
            'studygroup_id',
            'announcement_creator',
            'announcement_description',
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
            'studygroup_description',
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
            'invite_id',
            'creation_date',
            'expiration_date',
            'recipient',
            'studygroup_id',
        )