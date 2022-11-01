from turtle import pen
from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .UserFeedUtil import *

class GetUserFeed(ObtainAuthToken):
    """
    @ function
        Given a user token, return all the current activity of the user
    @ request Params
        user token: request.data['token']
    @ Return    
        The feed of the current user, this includes meedting creations, modules, study group info, etc.
    """
    def post(self, request, *args, **kwargs):
        """
        Given a Token -> Get user
        Get everything related to that user
            Sorted by Creation date
                //Later on we could look at ways of displaying information 
                  that is relavent to the user by some importance factor or time spent factor
        Merge each of the objects returned from the data base by creation date
        Loop through each entry to parse it into data fields
        
        Type..     
        StudyGroup -> 
                    Sub_Type.Info ... -> Announcement, Module Creation/Addition, Invite(Show exp date?), Material upload
                    Times/Dates ... -> When was the Sub_Type created ?
                    User ... -> Who created the Sub_Type ?

        Meeting -> 
                    Sub_Type.Info ... -> None
                    Times/Date ... -> Start time, End time, Date 
                    Users ... -> You and the other person

        Friend Request -> 
                    Sub_Type.Info ... -> None
                    Times/Date ... -> Time past since request
                    Users ... -> Who sent request?

        Course(Show new courses?) -> 
                    Sub_Type.Info ... -> Module uploads, General Course info(Subject, Description, Code)
                    Times/Date ... -> None
                    Users ... -> Owner

        Scholarships -> 
                    Sub_Type.Info ... -> GeneralInfo (Show type, Description)
                    Times/Date ... -> End date
                    Users ... -> Recomended by who?(prob not adding)

            Ex:
            Header-> {
                        Type : StudyGroup,
                        Name: {
                            case of Study group = study group name
                            case of Course = Course name
                            case of Scholarship = Scholarship name
                            case of Meeting = Null
                            case of Friend Request = Null
                        }
                    }
            Body->{
                    Sub_Type: {
                            case of Study group = Announcement, Module Creation/Addition, Invite(Show exp date?), Material upload
                            case of Course = Module uploads

                            else: None
                    }
                    Info: Announcement.description
                    Date: {
                        creation = creation.time
                        start = Start.time
                        end = Dnd.time
                    }
                    Users: {
                        Sender = Who made the thing
                        recipient = To everyone in group or just you
                    }
            }
            Oh my God this is hard / a lot
        """
 
        token = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token)[0].account
        
        queryset = []
        queryset = StudyGroupFeed(current_user) + MeetingFeed(current_user)


        queryset.sort(key=Content_Type_Date)
        
        send = {}
        #TODO:
        #Change index to be a more meaningful value
        index = 0
        for x in queryset:
           send[index] = Content_Type_Info(x)
           index = index + 1

        return Response(send)