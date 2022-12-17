from django.urls import path, include
from django.conf.urls import url
from backend.AllViews.AccountViews import *
from backend.AllViews.StudyGroupViews import *
from backend.AllViews.ModuleViews import *
from backend.AllViews.MaterialViews import *
from backend.AllViews.CourseViews import *
from backend.AllViews.UserFeedViews import *
from backend.AllViews.MeetingViews import *
from backend.AllViews.InviteViews import *
from backend.AllViews.AnnouncementViews import *
from backend.AllViews.ChatroomViews import *
from backend.AllViews.FriendsViews import *

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    #ACCOUNT VIEWS
    path('AccountCreation/', AccountCreation.as_view()),
    path('CurrentUser/', CurrentUser.as_view()),
    path('EditAccount/', EditAccount.as_view()),
    path('GetPerson/', GetPerson.as_view()),
    path('AllAccounts/', AllAccounts.as_view()),
    path('GetPeopleRole/', GetPeopleRole.as_view()),

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
    path('GetStudyGroup/', GetStudyGroup.as_view()),

    #MODULE VIWES
    path('CreateModule/', CreateModule.as_view()),
    path('GetAllModules/', GetAllModules.as_view()),
    path('GetModule/', GetModule.as_view()),
    
    #MATERIALVIEWS
    path('GetModuleMaterial/', GetModuleMaterial.as_view()),
    path('DeleteMaterial/', DeleteMaterial.as_view()),
    path('UpdateMaterial/', UpdateMaterial.as_view()),
    path('CreateMaterial/', CreateMaterial.as_view()),

    #COURSE VIEWS
    path('GetAllCourses/', GetAllCourses.as_view()),
    path('GetUsersInCourse/', GetUsersInCourse.as_view()),
    path('CreateCourse/', CreateCourse.as_view()),

    #FEED VIEWS
    path('GetUserFeed/', GetUserFeed.as_view()),
    path('GetFeedItem/', GetFeedItem.as_view()),

    #MEETING VIEWS
    path('CreateMeeting/', CreateMeeting.as_view()),
    path('GetUserMeetings/', GetUserMeetings.as_view()),
    path('DeleteMeeting/', DeleteMeeting.as_view()),
    path('GetOpenMeetingTimes/', GetOpenMeetingTimes.as_view()),

    #INVITE VIEWS
    path('CreateInvite/', CreateInvite.as_view()),
    path('GetInboundInvites/', GetInboundInvites.as_view()),
    path('GetOutboundInvites/', GetOutboundInvites.as_view()),
    path('GetGroupInvites/', GetGroupInvites.as_view()),
    path('DeleteInvite/', DeleteInvite.as_view()),

    #ANNOUNCEMENT VIEWS
    path('EnrolledGroupAnnouncements/', EnrolledGroupAnnouncements.as_view()),
    path('GetGroupAnnouncements/', GetGroupAnnouncements.as_view()),
    path('CreateAnnouncement/', CreateAnnouncement.as_view()),
    path('UpdateAnnouncement/', UpdateAnnouncement.as_view()),
    path('DeleteAnnouncement/', DeleteAnnouncement.as_view()),

    #CHATROOM VIEWS
    path('CreateMessage/', CreateMessage.as_view()),
    path('GetAllMessages/', GetAllMessages.as_view()),
    path('DeleteMessage/', DeleteMessage.as_view()),
    path('GetUserMessages/', GetUserMessages.as_view()),
    path('GetCurrentUserMessages/', GetCurrentUserMessages.as_view()),
    path('UpdateMessage/', UpdateMessage.as_view()),

    #FRIENDS VIEW
    path('SendFriendRequest/', SendFriendRequest.as_view()),
    path('GetAllFriends/', GetAllFriends.as_view()),
    path('AcceptFriendRequest/', AcceptFriendRequest.as_view()),
]