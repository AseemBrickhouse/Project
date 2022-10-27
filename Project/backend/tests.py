from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import *
from .AllViews.AccountViews import *
from .AllViews.ModuleViews import *
from .AllViews.StudyGroupViews import *


class TestAccount(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('login')
        self.user = "Ad"
        self.first_name = "Testing"
        self.last_name = "Admin"
        self.email = "Admin@uwm.edu"
        self.phone_number = 1234567890
        self.role = "ADMIN"

    def test_url(self):
        self.assertEquals(resolve(self.home_url).func.view_class, CurrentUser)

    def test_admin_post(self):
        Account.objects.create(user=self.user, first_name=self.first_name, last_name=self.last_name,
                               phone_number=self.phone_number, email=self.email, role=self.role)
        response = self.client.post(self.home_url, {'email': self.email, 'pw': self.password}, follow=True)
        self.assertEquals(response.status_code, 200, msg="GET Request to Admin Home Page Failed")


class TestMeeting(TestCase):
    def setUp(self):
        self.client = Client()
        self.AccountP.user = "Prof"
        self.AccountP.first_name = "Test"
        self.AccountP.last_name = "Professor"
        self.AccountP.email = "Professor@uwm.edu"
        self.AccountP.phone_number = 1234567890
        self.AccountP.role = "PROFESSOR"

        self.AccountS.user = "Tester"
        self.AccountS.first_name = "Test"
        self.AccountS.last_name = "Student"
        self.AccountS.email = "Student@uwm.edu"
        self.AccountS.phone_number = 1234567890
        self.AccountS.role = "STUDENT"

        self.Meeting.meeting_code = "123"
        self.Meeting.topic = "Math"
        self.Meeting.user1 = self.AccountP
        self.Meeting.user2 = self.AccountS
        self.Meeting.start_time = models.DateTimeField(blank=False, null=True)
        self.Meeting.end_time = models.DateTimeField(blank=False, null=True)


class TestCourse(TestCase):
    def setUp(self):
        self.client = Client()
        self.AccountP.user = "Prof"
        self.AccountP.first_name = "Test"
        self.AccountP.last_name = "Professor"
        self.AccountP.email = "Professor@uwm.edu"
        self.AccountP.phone_number = 1234567890
        self.AccountP.role = "PROFESSOR"

        self.AccountT.user = "Tutor"
        self.AccountT.first_name = "Test"
        self.AccountT.last_name = "Tutor"
        self.AccountT.email = "Tutor@uwm.edu"
        self.AccountT.phone_number = 1234567890
        self.AccountT.role = "TUTOR"

        self.Course.course_id = "123"
        self.Course.professor = self.AccountP
        self.Course.ta = self.AccountT
        self.Course.course_name = "MATH 100"
        self.Course.course_code = 123
        self.Course.course_description = "Introductory Math Course"


class TestStudyGroup(TestCase):
    def setUp(self):
        self.client = Client()

        self.AccountS.user = "Tester"
        self.AccountS.first_name = "Test"
        self.AccountS.last_name = "Student"
        self.AccountS.email = "Student@uwm.edu"
        self.AccountS.phone_number = 1234567890
        self.AccountS.role = "STUDENT"

        self.ChatRoom.chatroom_id = "54321"
        self.ChatRoom.chatroom_host = self.AccountS

        self.StudyGroup.studygroup_id = "1234"
        self.StudyGroup.invite_only = True
        self.StudyGroup.studygroup_host = self.AccountS
        self.StudyGroup.chat_id = self.ChatRoom.chatroom_id


class TestMaterial(TestCase):
    def setUp(self):
        self.client = Client()

        self.AccountP.user = "Prof"
        self.AccountP.first_name = "Test"
        self.AccountP.last_name = "Professor"
        self.AccountP.email = "Professor@uwm.edu"
        self.AccountP.phone_number = 1234567890
        self.AccountP.role = "PROFESSOR"

        self.ChatRoom.chatroom_id = "54321"
        self.ChatRoom.chatroom_host = self.AccountP

        self.StudyGroup.studygroup_id = "1234"
        self.StudyGroup.invite_only = True
        self.StudyGroup.studygroup_host = self.AccountP
        self.StudyGroup.chat_id = self.ChatRoom.chatroom_id

        self.Module.module_id = "135"
        self.Module.studygroup_id = self.StudyGroup.studygroup_id

        self.Material.material_id = "12345"
        self.Material.material_type = "QUIZ"
        self.Material.account = self.AccountP
        self.Material.module_id = self.Module.module_id
        self.Material.content = "Math 100 Quiz"
        self.Material.file_content = models.FileField(upload_to='images/', blank=True, null=True)
