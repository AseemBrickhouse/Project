#Handle all the frontend Links
#example: 127.0.0.8000/Classes
from django.urls import path
from .views import index
from django.conf.urls import url

urlpatterns = [
    path('', index),
    path('Login', index),
    path('Logout', index),
    path('AccountCreated', index),
    path('RecoveryPassword', index),
    path('RecoveryMessage', index),
    path('CreateAccount', index),
    path('AllStudyGroups', index),
    path('EnrolledStudyGroups', index),
    path('HostedStudyGroups', index),
    path('ScholarshipInformation', index),
    path('CreateStudyGroup', index),
    path('CreateStudyGroup', index),
    path('ViewProfile', index),
    path('EditProfile', index),
    path('PeopleHome/Students', index),
    path('PeopleHome/Instructors', index),
    path('PeopleHome/Tutors', index),
    path('CreateInvite', index),
    path('ViewInvite', index),
    path('CreateModule', index),
    url(r'ViewInvite/(?P<key>[a-zA-Z0-9]+.*)', index),
    url(r'ViewProfile/(?P<key>[a-zA-Z0-9]+.*)', index),
    url(r'StudyGroupHome/(?P<key>[a-zA-Z0-9]+.*)', index),
    url(r'StudyGroupHome/(?P<key>[a-zA-Z0-9]+.*)/Modules', index),
    url(r'StudyGroupHome/(?P<key>[a-zA-Z0-9]+.*)/Announcements', index),
    url(r'StudyGroupHome/(?P<key>[a-zA-Z0-9]+.*)/ChatRoom', index),
    url(r'StudyGroupHome/(?P<key>[a-zA-Z0-9]+.*)/CreateModule', index),
    path('SentRequest', index),
    path('ViewRequest',index),
    path('ViewFriends', index),
    # url(r'images/(?P<key>[a-zA-Z0-9]+.*)', index),
    path('test', index),
]