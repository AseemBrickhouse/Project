from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import random
import string


class CurrentUser(ObtainAuthToken):
    """
    @ function
        Retrives the current logged on user along with the information
    @ request Params
        user token: request.data['token']
    @ Return 
        All of the current users data in json format
    """
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        account = {}
        try:
            account = User.objects.all().filter(id=token)[0].account
        except User.DoesNotExist:
            return Response({
                "Error": "Return some error"
            })
        accountJson = AccountSerializer(account).data
        return Response(accountJson)
        
class AccountCreation(ObtainAuthToken):
    """
    @ function
        Given a user token create an account and link it to the user
    @ request Params
        user token: request.data['token']
        first name: request.data['first_name']
        last name: request.data['last_name']
        email: request.data['email']
    @ Return 
        Whether or not the account was successfully created
    """
    def post(self, request, *args, **kwargs):
        if request.data['token'] == None:
            return Response({
                "Message": "Token does not exists"
            })
        token_id = Token.objects.get(key=request.data['token']).user_id
        #Current User to create account for
        user = User.objects.all().filter(id=token_id)[0]
        try:
            account = Account.objects.get(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email']
            )
            return Response({
                "Message": "Account to create already exists"
            })
        except Account.DoesNotExist:
            account = Account.objects.create(
                user=user,
                key= ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
                phone_number= request.data['phone'] if request.data['phone'] != '' else 4444444444
            )
            account.save()

        return Response({"Message": "Account succesfully created"})

class EditAccount(ObtainAuthToken):
    """
    @ function
        Given a user token update the account information
    @ request Params
        user token: request.data['token']
        first name: request.data['first_name']
        last name: request.data['last_name']
        email: request.data['email']
        phone: request.data['phone']
        bio: request.data['bio']
    @ Return 
        Whether or not the account update was successfull
    """
    def put(self, request, *args, **kwargs):
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0]

        Account.objects.filter(user=current_user).update(
            first_name=request.data['first_name'] if request.data['first_name'] != "" else current_user.account.first_name,
            last_name=request.data['last_name'] if request.data['last_name'] != "" else current_user.account.last_name,
            phone_number=request.data['phone'] if request.data['phone'] != "" else current_user.account.phone_number,
            bio=request.data['bio'] if request.data['bio'] != "" else current_user.account.bio,
            email=request.data['email'] if request.data['email'] != "" else current_user.account.email,
            role=request.data['role'] if request.data['role'] != "" else current_user.account.role,
        )

        return Response({
            "Message": "Account information updated succesfully"
            })

class GetPerson(APIView):
    """
    @ function
        Retrive a selected user given the first,last, and email /// Can change to key later
    @ request Params
        first name: request.data['first_name']
        last name: request.data['last_name']
        email: request.data['email']
    @ Return 
        The persons info in json format if they exists
    """
    def post(self, request, *args, **kwargs):
        person_object = Account.objects.filter(
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            email = request.data['email'],
        )[0]
        person_json = AccountSerializer(person_object).data
 
        return Response(person_json)

class AllAccounts(APIView):
    """
    @ function
        Get all the current registered accounts
    @ request Params
        None
    @ Return 
        All accounts and info in json format
    """
    def get(self, request, *args, **kwargs):
        queryset = {}
        for account in Account.objects.all():
            account_json = AccountSerializer(account).data
            queryset[account_json['key']] = account_json

        return Response(queryset)


class GetPeopleRole(ObtainAuthToken):
    """
    @ function
        Retrive all selected user given the role
    @ request Params
        role: request.data['role]
    @ Return 
        The persons info in json format if they exists
    """
    def post(self, request, *args, **kwargs):
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0].account
        queryset = {}
        person_objects = Account.objects.all().exclude(key=current_user.key).filter(role=request.data['role'])
        print(person_objects)
        for person in person_objects:
            person_json = AccountSerializer(person).data
            queryset[person_json['key']] = person_json
            # queryset[person_json['key']]['key'] = person_json['key']
        # person_json = AccountSerializer(person_object).data
        # if request.data['token'] != None:
        #     #TODO:
        #     #Implement for friends later
        #     pass
        print(queryset)
        return Response(queryset)