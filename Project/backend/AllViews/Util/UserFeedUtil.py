from ...serilizers import *
from ...models import *


def StudyGroupFeed(current_user):
    """
    @ function
        Given the current user return all of the objects related to all the study groups the user is in
    @ request Params
        current_user: Account object
    @ Return    
        All objects related to the study groups the user is in. -> Type [<Invite: Object> | <Module: Object> | <Announcement: Object>]
    """
    queryset = []
    enrolled_studygroups = {}
    for enroll in StudyEnroll.objects.all().filter(account=current_user):
        studygroup_json = StudyGroupSerilizer(enroll.studygroup_id).data
        enrolled_studygroups[studygroup_json['studygroup_id']] = studygroup_json

    for group in enrolled_studygroups:
        group_info = enrolled_studygroups[group]
        for announcement in Announcements.objects.all().filter(studygroup_id=group_info['id']):
            queryset.append(announcement)
        # for module in Module.objects.all().filter(studygroup_id=group_info['id']):
        #     queryset.append(module)

    for invite in Invite.objects.all().filter(recipient=current_user):
        queryset.append(invite)

    return queryset

def MeetingFeed(current_user):
    """
    @ function
        Given the current user return all the meetings the user in is
    @ request Params
        current_user: Account object
    @ Return    
        All meetings the user is in. -> Type [<Meeting: Object>]
    """
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
    """
    @ function
        Given a random model, find out what model is being called and return the creation date of the model object.
        Mainly used for a key for sorting the Object List
    @ request Params
        model_obj: random model
    @ Return    
        Creation date of the model.
    """
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
    """
    @ function
        Given a random model, find out what model is being called -> Parse the data into tuples -> Format the data in the correct json fields -> return formmated json 
        Mainly used for a key for sorting the Object List
    @ request Params
        model_obj: random model
    @ Return    
        Formattted json of the given model object
    """
    def Format_data(header, body):
        print(body[2][2])
        template = {
            "Header": {
                "id":   header[0],
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

            studygroup = StudyGroup.objects.all().get(id=announcement_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data
            
            user = Account.objects.all().get(id=announcement_json['announcement_creator'])
            user_json = AccountSerilizer(user).data
            user_name = user_json['first_name'] + user_json['last_name']

            header = (
                announcement_json['id'],
                "StudyGroup",
                announcement_json['announcement_id'],
                studygroup_json['studygroup_name'],
            )
            body = (
                ("Announcement"),
                (announcement_json['announcement_description']),
                (announcement_json['creation_date'], None, None),
                (user_name, user_json, None, None)
            )
            return Format_data(header, body)
        case "Invite":
            invite_json = InviteSerlizer(model_obj).data

            studygroup = StudyGroup.objects.all().get(id=invite_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data

            sender_obj = Account.objects.all().filter(id=invite_json['sender'])[0]
            sender_info = AccountSerilizer(sender_obj).data
            sender = sender_info['first_name'] + sender_info['last_name']

            recipient_obj = Account.objects.all().filter(id=invite_json['recipient'])[0]
            recipient_info = AccountSerilizer(recipient_obj).data
            recipient = recipient_info['first_name'] + recipient_info['last_name']

            description = "Studygroup invite to " + studygroup_json['studygroup_name']
            header = (
                invite_json['id'],
                "StudyGroup",
                invite_json['invite_id'],
                studygroup_json['studygroup_name'],
            )
            body = (
                ("Invite"),
                (description),
                (invite_json['creation_date'], invite_json['creation_date'], invite_json['expiration_date']),
                (sender, sender_info, recipient, recipient_info),
            )
            return Format_data(header, body)

        case "Module":
            #TODO:
            # When Module is more developed
            # Get all material objects given the Module id -> parse data -> format in description
            return ModuleSerilizer(model_obj).data

        #Prob no need for Material seeing its part of modules
        case "Material":
            pass
        
        #Meeting
        case "Meeting":
            meeting_json = MeetingSerilizer(model_obj).data

            sender_obj = Account.objects.all().filter(id=meeting_json['user1'])[0]
            sender_info = AccountSerilizer(sender_obj).data
            sender = sender_info['first_name'] + sender_info['last_name']

            recipient_obj = Account.objects.all().filter(id=meeting_json['user2'])[0]
            recipient_info = AccountSerilizer(recipient_obj).data
            recipient = recipient_info['first_name'] + recipient_info['last_name']

            header = (
                meeting_json['id'],
                "Meeting",
                meeting_json['meeting_code'],
                None,
            )
            body = (
                (None),
                (meeting_json['topic']),
                (meeting_json['creation_date'], meeting_json['start_time'], meeting_json['end_time']),
                (sender, sender_info, recipient, recipient_info),
            )
            return Format_data(header, body)

        #Course
        case "Course_Module":
            pass
        
def Content_Type_View(sub_type, id):
    match sub_type:
        #Study group
        case "Announcements" | "Announcement":
            announcement = Announcements.objects.all().get(announcement_id=id)
            announcement_json = AnnouncementSerilizer(announcement).data

            studygroup = StudyGroup.objects.all().get(id=announcement_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data

            queryset = {
                studygroup_json['studygroup_id']: studygroup_json,
                announcement_json['announcement_id']: announcement_json
            }
            return queryset

        case "Invite":
            invite = Invite.objects.all().get(invite_id=id)
            invite_json = InviteSerlizer(invite).data

            studygroup = StudyGroup.objects.all().get(id=invite_json['studygroup_id'])
            studygroup_json = StudyGroupSerilizer(studygroup).data

            queryset = {
                studygroup_json['studygroup_id']: studygroup_json,
                invite_json['invite_id']: invite_json
            }            
            return queryset

        #Still thinking of some logic for this
        case "Module":
            pass
        case "Material":
            pass

        #Meeting
        case "Meeting":
            meeting = Meeting.objects.all().get(meeting_code=id)
            meeting_json = MeetingSerilizer(meeting).data

            user1 = Account.objects.all().get(id=meeting_json['user1'])
            user1_json = AccountSerilizer(user1).data

            user2 = Account.objects.all().get(id=meeting_json['user2'])
            user2_json = AccountSerilizer(user2).data

            queryset = {
                meeting_json['meeting_code']: meeting_json,
                user1_json['key']: user1_json,
                user2_json['key']: user2_json
            }
            
            return queryset

        #Course
        case "Course_Module":
            pass