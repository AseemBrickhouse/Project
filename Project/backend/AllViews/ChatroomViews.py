from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from datetime import datetime
import random
import string

class GetAllMessages(APIView):
    def post(self, request, *args, **kwargs):
        pass

class CreateMessage(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        pass

class DeleteMessage(ObtainAuthToken):
    def delete(self, request, *args, **kwargs):
        pass

class GetUserMessages(APIView):
    def post(self, request, *args, **kwargs):
        pass

class GetCurrentUserMessages(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        pass

