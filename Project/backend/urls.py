from django.urls import path, include
from django.conf.urls import url
from backend.AllViews.AccountViews import *
from backend.AllViews.StudyGroupViews import *
from backend.AllViews.ModuleViews import *

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
    path('GetUserHostedGroups/', GetUserHostedGroups.as_view()),
    path('DeleteStudyGroup/', DeleteStudyGroup.as_view()),
    path('GetUsersInGroup/', GetUsersInGroup.as_view()),
    path('LeaveStudyGroup/', LeaveStudyGroup.as_view()),
    path('GetGroupModules/', GetGroupModules.as_view()),

    #MODULE VIWES
    path('CreateModule/', CreateModule.as_view()),
    path('GetAllModules/', GetAllModules.as_view()),
]