import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class roles(models.TextChoices): 
    admin = "ADMIN"
    professor = "PROFESSOR"
    student = "STUDENT"
    tutor = "TUTOR"


class Account(models.Model):
    key = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.IntegerField(blank=True)
    role = models.CharField(max_length=10,choices=roles.choices)

class Meeting(models.Model):
    meeting_code = models.CharField(max_length=20)
    user1 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user2")

class Course(models.Model):
    course_id = models.CharField(max_length=20)
    professor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="professor")
    ta = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="ta")
    course_name = models.CharField(max_length=30, null=True)
    course_code = models.IntegerField(null=True)

class CourseEnroll(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Message(models.Model):
    message_id = models.CharField(max_length=20)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()

class ChatRoom(models.Model):
    chatroom_id = models.CharField(max_length=20)
    chatroom_host = models.ForeignKey(Account, on_delete=models.CASCADE)
    messages = models.ForeignKey(Message, on_delete=models.CASCADE, blank=True, null=True)

class StudyGroup(models.Model):
    studygroup_id = models.CharField(max_length=20, null=True)
    studygroup_host = models.ForeignKey(Account, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

class StudyEnroll(models.Model):
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE,null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Material(models.Model):
    material_id = models.CharField(max_length=20)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    studygroup_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, null=True)
    content = models.TextField()