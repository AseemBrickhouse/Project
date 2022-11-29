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
    path('ScholarshipInformation', index),
    path('CreateStudyGroup', index),
    path('CreateStudyGroup', index),
    url(r'StudyGroupHome/(?P<key>[a-zA-Z0-9]+.*)', index),
]