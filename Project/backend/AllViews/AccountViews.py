from rest_framework import viewsets
from ..serilizers import *
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
        accountJson = AccountSerilizer(account).data
        return Response(accountJson)
        
class AccountCreation(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token_id = Token.objects.get(key=request.data['token']).user_id
        #Current User to create account for
        user = User.objects.all().filter(id=token_id)[0]
        try:
            account = Account.objects.get(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email']
            )
        except Account.DoesNotExist:
            pass

        account = Account.objects.create(
            user=user,
            key= ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            phone_number= request.data['phone'] if  request.data['phone'] != '' else None
        )
        account.save()

        return Response (request.data)

class EditAccount(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token_id = Token.objects.get(key=request.data['token']).user_id
        current_user = User.objects.all().filter(id=token_id)[0]

        Account.objects.filter(user=current_user).update(
            first_name=request.data['first_name'] if request.data['first_name'] != "" else current_user.account.first_name,
            last_name=request.data['last_name'] if request.data['last_name'] != "" else current_user.account.last_name,
            phone=request.data['phone'] if request.data['phone'] != "" else current_user.account.phone,
            bio=request.data['bio'] if request.data['bio'] != "" else current_user.account.bio,
            email=request.data['email'] if request.data['email'] != "" else current_user.account.email,
        )

        return Response(request.data)

class GetPerson(APIView):
    def post(self, request, *args, **kwargs):
        person_object = Account.objects.filter(
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            email = request.data['email'],
        )[0]
        person_json = AccountSerilizer(person_object).data
        if request.data['token'] != None:
            #TODO:
            #Implement for friends later
            pass

        return Response(person_json)

class AllAccounts(APIView):
    def get(self, request, *args, **kwargs):
        queryset = {}
        for account in Account.objects.all():
            account_json = AccountSerilizer(account).data
            queryset[account_json['key']] = account_json

        return Response(queryset)