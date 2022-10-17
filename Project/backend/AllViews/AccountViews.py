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
            key= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)),
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            phone_number= request.data['phone'] if  request.data['phone'] != '' else None
        )
        account.save()

        return Response (request.data)