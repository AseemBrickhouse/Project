from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import *
from .AllViews.AccountViews import *
from .AllViews.AnnouncementViews import *
from .AllViews.CourseViews import *
from .AllViews.ChatroomViews import *
from .AllViews.InviteViews import *
from .AllViews.MeetingViews import *
from .AllViews.ModuleViews import *
from .AllViews.StudyGroupViews import *


class TestAccount(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = "Ad"
        self.first_name = "Testing"
        self.last_name = "Admin"
        self.email = "Admin@uwm.edu"
        self.phone_number = 1234567890
        self.role = "ADMIN"

        self.prof_user = "Prof"
        self.prof_first_name = "Test"
        self.prof_last_name = "Professor"
        self.prof_email = "Professor@uwm.edu"
        self.prof_phone_number = 1234567890
        self.prof_role = "PROFESSOR"

        self.tutor_user = "Tutor"
        self.tutor_first_name = "Test"
        self.tutor_last_name = "Tutor"
        self.tutor_email = "Tutor@uwm.edu"
        self.tutor_phone_number = 1234567890
        self.tutor_role = "TUTOR"

        self.student_user = "Tester"
        self.student_first_name = "Test"
        self.student_last_name = "Student"
        self.student_email = "Student@uwm.edu"
        self.student_phone_number = 1234567890
        self.student_role = "STUDENT"

    def test_url(self):
        self.assertEquals(resolve('Login').func.view_class, CurrentUser)

    def test_adminCreate_post(self):
        Account.objects.create(user=self.user, first_name=self.first_name, last_name=self.last_name,
                               phone_number=self.phone_number, email=self.email, role=self.role)
        response = self.client.post('CreateAccount',
                                    {'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email,
                                     'phone': self.phone_number}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateAccount")
        existingUser = Account.objects.get(first_name=self.first_name)
        self.assertEquals(existingUser.first_name, self.first_name, msg="Names do not match from database")

    def test_profCreate_post(self):
        Account.objects.create(user=self.prof_user, first_name=self.prof_first_name, last_name=self.prof_last_name,
                               phone_number=self.prof_phone_number, email=self.prof_email, role=self.prof_role)
        response = self.client.post('CreateAccount',
                                    {'first_name': self.prof_first_name, 'last_name': self.prof_last_name,
                                     'email': self.prof_email,
                                     'phone': self.prof_phone_number}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateAccount")
        existingUser = Account.objects.get(first_name=self.prof_first_name)
        self.assertEquals(existingUser.first_name, self.prof_first_name, msg="Names do not match from database")

    def test_tutorCreate_post(self):
        Account.objects.create(user=self.tutor_user, first_name=self.tutor_first_name, last_name=self.tutor_last_name,
                               phone_number=self.tutor_phone_number, email=self.tutor_email, role=self.tutor_role)
        response = self.client.post('CreateAccount',
                                    {'first_name': self.tutor_first_name, 'last_name': self.tutor_last_name,
                                     'email': self.tutor_email,
                                     'phone': self.tutor_phone_number}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateAccount")
        existingUser = Account.objects.get(first_name=self.tutor_first_name)
        self.assertEquals(existingUser.first_name, self.tutor_first_name, msg="Names do not match from database")

    def test_studentCreate_post(self):
        Account.objects.create(user=self.student_user, first_name=self.student_first_name,
                               last_name=self.student_last_name,
                               phone_number=self.student_phone_number, email=self.student_email, role=self.student_role)
        response = self.client.post('CreateAccount',
                                    {'first_name': self.student_first_name, 'last_name': self.student_last_name,
                                     'email': self.student_email,
                                     'phone': self.student_phone_number}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateAccount")
        existingUser = Account.objects.get(first_name=self.student_first_name)
        self.assertEquals(existingUser.first_name, self.student_first_name, msg="Names do not match from database")

    def test_editAccount_post(self):
        Account.objects.create(user=self.student_user, first_name=self.student_first_name,
                               last_name=self.student_last_name,
                               phone_number=self.student_phone_number, email=self.student_email, role=self.student_role)
        response = self.client.post('EditAccount/',
                                    {'first_name': self.student_first_name, 'last_name': self.student_last_name,
                                     'email': self.student_email,
                                     'phone': self.student_phone_number, 'bio': "bio test"}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in editAccount")
        existingUser = Account.objects.get(first_name=self.student_first_name)
        self.assertEquals(existingUser.bio, "bio test", msg="Bios do not match from database")


class TestAnnouncement(TestCase):
    def setUp(self):
        self.client = Client()

        self.student_user = "Tester"
        self.student_first_name = "Test"
        self.student_last_name = "Student"
        self.student_email = "Student@uwm.edu"
        self.student_phone_number = 1234567890
        self.student_role = "STUDENT"

        self.chatroom_id = "54321"
        self.chatroom_host = self.student_user

        self.studygroup_id = "1234"
        self.invite_only = True
        self.studygroup_host = self.student_user
        self.chat_id = self.chatroom_id

        self.announcement_id = "123"
        self.announcement_creator = self.student_user
        self.announcement_description = "test announcement"

    def test_url(self):
        self.assertEquals(resolve('CreateAnnouncement/').func.view_class, CreateAnnouncement)

    def test_createAnnouncement(self):
        Announcements.objects.create(announcement_id=self.announcement_id, studygroup_id=self.studygroup_id,
                                     announcement_creator=self.announcement_creator,
                                     chat_id=self.announcement_description)
        response = self.client.post('CreateAnnouncement/',
                                    {'announcement_description': self.announcement_description}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in createAnnouncement")
        existingAnnouncement = Account.objects.get(announcement_description=self.announcement_description)
        self.assertEquals(existingAnnouncement.announcement_description, "test announcement",
                          msg="Announcements do not match from database")


class TestChatroom(TestCase):
    def setUp(self):
        self.client = Client()

        self.student_user = "Tester"
        self.student_first_name = "Test"
        self.student_last_name = "Student"
        self.student_email = "Student@uwm.edu"
        self.student_phone_number = 1234567890
        self.student_role = "STUDENT"

        self.chatroom_id = "54321"
        self.chatroom_host = self.student_user

        self.studygroup_id = "1234"
        self.invite_only = True
        self.studygroup_host = self.student_user
        self.chat_id = self.chatroom_id

        self.message_id = "1234"
        self.creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        self.account = self.student_user
        self.content = "testing message"

    def test_url(self):
        self.assertEquals(resolve('CreateMessage/').func.view_class, CreateMessage)

    def test_createMessage(self):
        Message.objects.create(message_id=self.message_id, chatroom_id=self.chatroom_id,
                               creation_date=self.creation_date, account=self.account, content=self.content)
        response = self.client.post('CreateMessage/',
                                    {'message': self.content}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in createAnnouncement")
        existingMessage = Message.objects.get(content=self.content)
        self.assertEquals(existingMessage.content, "testing message", msg="messages do not match from database")


class TestCourse(TestCase):
    def setUp(self):
        self.client = Client()
        self.prof_user = "Prof"
        self.prof_first_name = "Test"
        self.prof_last_name = "Professor"
        self.prof_email = "Professor@uwm.edu"
        self.prof_phone_number = 1234567890
        self.prof_role = "PROFESSOR"

        self.tutor_user = "Tutor"
        self.tutor_first_name = "Test"
        self.tutor_last_name = "Tutor"
        self.tutor_email = "Tutor@uwm.edu"
        self.tutor_phone_number = 1234567890
        self.tutor_role = "TUTOR"

        self.course_id = "123"
        self.professor = self.prof_user
        self.ta = self.tutor_user
        self.course_name = "MATH 100"
        self.course_code = 123
        self.course_description = "Introductory Math Course"

    def test_url(self):
        self.assertEquals(resolve('CreateCourse/').func.view_class, CreateCourse)

    def test_createCourse(self):
        Course.objects.create(course_id=self.course_id, professor=self.professor, ta=self.ta,
                              course_name=self.course_name,
                              course_code=self.course_code, course_description=self.course_description)
        response = self.client.post('CreateCourse/',
                                    {'course_owner': self.professor, 'course_name': self.course_name,
                                     'course_code': self.course_code}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateAccount")
        existingCourse = Course.objects.get(course_name=self.course_name)
        self.assertEquals(existingCourse.course_name, self.course_name, msg="Names do not match from database")


class TestInvite(TestCase):
    def setUp(self):
        self.client = Client()

        self.student_user = "Tester"
        self.student_first_name = "Test"
        self.student_last_name = "Student"
        self.student_email = "Student@uwm.edu"
        self.student_phone_number = 1234567890
        self.student_role = "STUDENT"

        self.student2_user = "Tester2"
        self.student2_first_name = "Test2"
        self.student2_last_name = "Student2"
        self.student2_email = "Student2@uwm.edu"
        self.student2_phone_number = 2123456789
        self.student2_role = "STUDENT2"

        self.chatroom_id = "54321"
        self.chatroom_host = self.student_user

        self.studygroup_id = "1234"
        self.invite_only = True
        self.studygroup_host = self.student_user
        self.chat_id = self.chatroom_id

        self.invite_id = "1234"
        self.sender = self.student_user
        self.creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        self.expiration_date = models.DateTimeField(blank=True, null=True)
        self.recipient = self.student2_user

    def test_url(self):
        self.assertEquals(resolve('CreateInvite/').func.view_class, CreateInvite)

    def test_createInvite(self):
        Invite.objects.create(invite_id=self.invite_id, sender=self.sender, creation_date=self.creation_date,
                              expiration_date=self.expiration_date, recipient=self.recipient,
                              studygroup_id=self.studygroup_id)
        response = self.client.post('CreateInvite/', follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateInvite")
        existingInvite = Invite.objects.get(invite_id=self.invite_id)
        self.assertEquals(existingInvite.invite_id, self.invite_id, msg="invite IDs do not match from database")


class TestMeeting(TestCase):
    def setUp(self):
        self.client = Client()
        self.prof_user = "Prof"
        self.prof_first_name = "Test"
        self.prof_last_name = "Professor"
        self.prof_email = "Professor@uwm.edu"
        self.prof_phone_number = 1234567890
        self.prof_role = "PROFESSOR"

        self.student_user = "Tester"
        self.student_first_name = "Test"
        self.student_last_name = "Student"
        self.student_email = "Student@uwm.edu"
        self.student_phone_number = 1234567890
        self.student_role = "STUDENT"

        self.meeting_code = "123"
        self.creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        self.topic = "Math"
        self.user1 = self.prof_user
        self.user2 = self.student_user
        self.start_time = models.DateTimeField(blank=False, null=True)
        self.end_time = models.DateTimeField(blank=False, null=True)

    def test_url(self):
        self.assertEquals(resolve('CreateMeeting/').func.view_class, CreateMeeting)

    def test_createMeeting(self):
        Meeting.objects.create(meeting_code=self.meeting_code, creation_date=self.creation_date, topic=self.topic, user1=self.user1, user2=self.user2, start_time=self.start_time, end_time=self.end_time)
        response = self.client.post('CreateMeeting/',
                                    {'topic': self.topic}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateMeeting")
        existingMeeting = Meeting.objects.get(topic=self.topic)
        self.assertEquals(existingMeeting.topic, "Math", msg="invite IDs do not match from database")


class TestModule(TestCase):
    def setUp(self):
        self.client = Client()

        self.prof_user = "Prof"
        self.prof_first_name = "Test"
        self.prof_last_name = "Professor"
        self.prof_email = "Professor@uwm.edu"
        self.prof_phone_number = 1234567890
        self.prof_role = "PROFESSOR"

        self.chatroom_id = "54321"
        self.chatroom_host = self.prof_user

        self.studygroup_id = "1234"
        self.invite_only = True
        self.studygroup_host = self.prof_user
        self.chat_id = self.chatroom_id

        self.module_id = "135"
        self.creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        self.module_owner = self.prof_user
        self.studygroup_id = self.studygroup_id

        self.material_id = "12345"
        self.material_type = "QUIZ"
        self.account = self.prof_user
        self.module_id = self.module_id
        self.content = "Math 100 Quiz"
        self.file_content = models.FileField(upload_to='images/', blank=True, null=True)

    def test_url(self):
        self.assertEquals(resolve('CreateModule/').func.view_class, CreateModule)

    def test_createModule(self):
        Module.objects.create(module_id=self.module_id, creation_date=self.creation_date, module_owner=self.module_owner, studygroup_id=self.studygroup_id)
        response = self.client.post('CreateModule/', follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateModule")
        existingModule = Module.objects.get(module_id=self.module_id)
        self.assertEquals(existingModule.module_id, self.module_id, msg="invite IDs do not match from database")



class TestStudyGroup(TestCase):
    def setUp(self):
        self.client = Client()

        self.student_user = "Tester"
        self.student_first_name = "Test"
        self.student_last_name = "Student"
        self.student_email = "Student@uwm.edu"
        self.student_phone_number = 1234567890
        self.student_role = "STUDENT"

        self.chatroom_id = "54321"
        self.chatroom_host = self.student_user

        self.studygroup_id = "1234"
        self.invite_only = True
        self.studygroup_host = self.student_user
        self.chat_id = self.chatroom_id

    def test_url(self):
        self.assertEquals(resolve('api/CreateStudyGroup/').func.view_class, CreateStudyGroup)

    def test_createStudyGroup(self):
        StudyGroup.objects.create(studygroup_id=self.studygroup_id, invite_only=self.invite_only,
                                  studygroup_host=self.studygroup_host, chat_id=self.chat_id)
        response = self.client.post('CreateStudyGroup/',
                                    {'studygroup_name': "group1", 'chatroom_id': self.chatroom_id,
                                     'chatroom_host': self.chatroom_host, 'studygroup_id': self.studygroup_id,
                                     'account': self.student_user}, follow=True)
        self.assertEquals(response.status_code, 200, msg="Return some error in CreateStudyGroup")
        existingStudyGroup = StudyGroup.objects.get(studygroup_id=self.studygroup_id)
        self.assertEquals(existingStudyGroup.studygroup_id, self.studygroup_id, msg="IDs do not match from database")