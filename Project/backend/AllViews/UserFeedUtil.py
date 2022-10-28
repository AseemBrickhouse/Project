from pipes import Template
from ..serilizers import *
from ..models import *

def StudyGroupFeed(current_user):
    queryset = []
    enrolled_studygroups = {}
    for enroll in StudyEnroll.objects.all().filter(account=current_user):
        studygroup_json = StudyGroupSerilizer(enroll.studygroup_id).data
        enrolled_studygroups[studygroup_json['studygroup_id']] = studygroup_json

    for group in enrolled_studygroups:
        group_info = enrolled_studygroups[group]
        for announcement in Announcements.objects.all().filter(studygroup_id=group_info['id']):
            queryset.append(announcement)
        for module in Module.objects.all().filter(studygroup_id=group_info['id']):
            queryset.append(module)

    for invite in Invite.objects.all().filter(recipient=current_user):
        queryset.append(invite)

    return queryset

def MeetingFeed(current_user):
    queryset = []
    all_meetings = Meeting.objects.all().filter(user1=current_user) | Meeting.objects.all().filter(user2=current_user)
    for meeting in all_meetings:
        queryset.append(meeting)
    return queryset

def FriendRequestFeed(current_user):
    pass

def Scholarships():
    pass

def Course():
    pass

def Content_Type_Date(model_obj):
    model_name = model_obj.__class__.__name__

    match model_name:

        #Study group
        case "Announcements":
            return AnnouncementSerilizer(model_obj).data['creation_date']
        case "Invite":
            return InviteSerlizer(model_obj).data['creation_date']
        case "Module":
            return ModuleSerilizer(model_obj).data['creation_date']
        case "Material":
            pass

        #Meeting
        case "Meeting":
            return MeetingSerilizer(model_obj).data['creation_date']

        #Course
        case "Course_Module":
            pass
        
def Content_Type_Info(model_obj):
    def Format_data(header, body):
        print(body[2][2])
        template = {
            "Header": {
                "id": header[0],
                "Type": header[1],
                "Key":  header[2],
                "Name": header[3],
            },
            "Body":{
                "Sub_Type": {
                    "Type": body[0],
                },
                "Info":{
                    "Description": body[1],
                },
                "Dates":{
                    "Creation_date":  body[2][0],
                    "Start_date":  body[2][1],
                    "End_date":  body[2][2],
                },
                "Users":{
                    "Sender": {
                        "Name": body[3][0],
                        "Info": body[3][1],
                    },
                    "Recipient":{ 
                        "Name": body[3][2],
                        "Info": body[3][3],
                    }
                }
            },
        }
        return template

    model_name = model_obj.__class__.__name__
    match model_name:
        #Study group
        case "Announcements":
            announcement_json = AnnouncementSerilizer(model_obj).data
            header = (
                announcement_json['id'],
                "StudyGroup",
                announcement_json['announcement_id'],
                None,
            )
            body = (
                ("Announcement"),
                #add model field for announcement data
                (None),
                (announcement_json['creation_date'], None, None),
                 #Add creator model field
                (None, None, None, None)
            )
            return Format_data(header, body)
        case "Invite":
            invite_json = InviteSerlizer(model_obj).data

            sender_obj = Account.objects.all().filter(id=invite_json['sender'])[0]
            sender_info = AccountSerilizer(sender_obj).data
            sender = sender_info['first_name'] + sender_info['last_name']

            recipient_obj = Account.objects.all().filter(id=invite_json['recipient'])[0]
            recipient_info = AccountSerilizer(recipient_obj).data
            recipient = recipient_info['first_name'] + recipient_info['last_name']

            header = (
                invite_json['id'],
                "StudyGroup",
                #Have to Add id field for invites invite_json['invite_id'],
                None,
                None,
            )
            body = (
                ("Invite"),
                (None),
                (invite_json['creation_date'], None, invite_json['expiration_date']),
                (sender, sender_info, recipient, recipient_info),
            )
            return Format_data(header, body)
        case "Module":
            return ModuleSerilizer(model_obj).data
        case "Material":
            pass
        
        #Meeting
        case "Meeting":
            return MeetingSerilizer(model_obj).data

        #Course
        case "Course_Module":
            pass
        