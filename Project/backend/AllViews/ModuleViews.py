from ..serilizers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
import random
import string

class GetAllModules(APIView):
    def get(self, request, *args, **kwargs):
        modules = Module.objects.all()

        queryset = {}

        for module in modules:
            moduleJSON = ModuleSerilizer(module).data
            queryset[moduleJSON['module_id']] = moduleJSON

        return Response(queryset)

class CreateModule(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account
        #error handle later
        studygroupJSON = StudyGroupSerilizer(studygroup).data
        module_toCreate = Module.objects.create(
            module_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            module_owner = currentUser,
            studygroup_id = studygroup,
        )

        module_toCreate.save()

        return Response({
            "Message": "Module succesfully created for study group " +  studygroupJSON['studygroup_id']
        })