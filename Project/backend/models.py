from django.db import models
from django.contrib.auth.models import User

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
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.IntegerField(blank=True)
    role = models.CharField(max_length=10,choices=roles.choices)
    bio = models.TextField(null=True)
    somenewField = models.TextField(null=True)
    # INSTALL PILLOW!!!
    # profile_pic = models.ImageField(blank=True, null=True)

class Friends(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account")
    friends_with = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="friends_with")
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)

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
    professor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="professor")
    ta = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="ta")
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
    invite_only = models.BooleanField(blank = True, null = True, default = False)
    studygroup_host = models.ForeignKey(Account, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

class Module(models.Model):
    module_id = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)

class Announcements(models.Model):
    announcement_id = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)

class StudyEnroll(models.Model):
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Material(models.Model):
    material_id = models.CharField(max_length=20)
    material_type = models.CharField(max_length=20,choices=type.choices, null = True)
    creation_date = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    content = models.TextField(null = True, blank = True)
    file_content = models.FileField(upload_to='images/', blank=True, null=True)