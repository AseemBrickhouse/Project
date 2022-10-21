from django.urls import path, include
from django.conf.urls import url
from backend.AllViews.AccountViews import *
from backend.AllViews.StudyGroupViews import *

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    #ACCOUNT VIEWS
    path('AccountCreation/', AccountCreation.as_view()),
    path('CurrentUser/', CurrentUser.as_view()),

    #STUDYGROUP VIEWS
    path('GetAllStudyGroups/', GetAllStudyGroups.as_view()),
    path('CreateStudyGroup/', CreateStudyGroup.as_view()),
    path('GetAllUserStudyGroups/', GetAllUserStudyGroups.as_view()),
    path('JoinStudyGroup/', JoinStudyGroup.as_view()),
]