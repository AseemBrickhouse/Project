from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
# Create your models here.

class roles(models.TextChoices): 
    admin = "ADMIN"
    professor = "PROFESSOR"
    student = "STUDENT"
    tutor = "TUTOR"

class type(models.TextChoices): 
    quiz = "QUIZ"
    exam = "EXAM"
    studyguide = "STUDYGUIDE"
    homework = "HOMEWORK"
    disscussion_post = "DISSCUSSION_POST"


class Account(models.Model):
    key = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=26, default="first")
    last_name = models.CharField(max_length=26, default="last")
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.IntegerField(blank=True)
    role = models.CharField(max_length=10,choices=roles.choices)
    bio = models.TextField(null=True)
    # INSTALL PILLOW!!!
    profile_pic = models.ImageField(blank=True, null=True)

class Friends(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="user_account")
    friends = models.ManyToManyField(Account, related_name="friends")
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)

class FriendRequest(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    from_user = models.ForeignKey(Account, on_delete=models.CASCADE, blank = True, null= True, related_name="from_user")
    to_user = models.ForeignKey(Account, on_delete=models.CASCADE, blank = True, null= True, related_name="to_user")
    

class Meeting(models.Model):
    meeting_code = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    topic = models.TextField(max_length=1000, null=True)
    user1 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user2")
    start_time = models.DateTimeField(blank = False, null = True)
    end_time = models.DateTimeField(blank = False, null = True)

class Course(models.Model):
    course_id = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    course_owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="course_owner", null=True, blank=True)
    professor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="professor", null=True, blank=True)
    ta = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="ta", null=True, blank=True)
    course_name = models.CharField(max_length=30, null=True)
    course_code = models.IntegerField(null=True)
    course_description = models.TextField(max_length=10000, null=True, blank = True)

class CourseEnroll(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class ChatRoom(models.Model):
    chatroom_id = models.CharField(max_length=20)
    chatroom_host = models.ForeignKey(Account, on_delete=models.CASCADE)

class Message(models.Model):
    message_id = models.CharField(max_length=20)
    chatroom_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()

class StudyGroup(models.Model):
    studygroup_id = models.CharField(max_length=20, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    studygroup_name = models.CharField(max_length=50, blank = False, null = True)
    invite_only = models.BooleanField(blank = True, null = True, default = False)
    studygroup_host = models.ForeignKey(Account, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    studygroup_description=models.TextField(null=True, blank=True)

class Module(models.Model):
    module_id = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    module_owner = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)

class Announcements(models.Model):
    announcement_id = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)
    announcement_creator = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    announcement_description = models.TextField(null=True, blank=True)

class StudyEnroll(models.Model):
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Material(models.Model):
    #FIX IN FUTURE
    # def path():
    #     return os.path.join(settings.MEDIA_ROOT_STUDYGROUP)
    material_id = models.CharField(max_length=20)
    material_type = models.CharField(max_length=20,choices=type.choices, null = True)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    content = models.TextField(null = True, blank = True)
    #Change upload_to -> FIX TO PLACE FILES IN DIFFERENT FOLDERS RATHER THAN 1 FOLDER
    # file_content = models.FilePathField(path=' ', blank=True, null=True)
    file_content_upload = models.FileField(upload_to='images/', blank=True, null=True)

class Invite(models.Model):
    invite_id = models.CharField(max_length=20, blank=True, null=True)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="sender")
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    expiration_date = models.DateTimeField(blank = True, null=True)
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="recipient")
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)