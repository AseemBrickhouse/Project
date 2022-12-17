from ..serializers import *
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
            moduleJSON = ModuleSerializer(module).data
            queryset[moduleJSON['module_id']] = moduleJSON

        return Response(queryset)

class CreateModule(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        studygroup = StudyGroup.objects.all().get(studygroup_id=request.data['studygroup_id'])
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account
        #error handle later
        studygroupJSON = StudyGroupSerializer(studygroup).data
        module_toCreate = Module.objects.create(
            module_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            module_owner = currentUser,
            studygroup_id = studygroup,
        )

        module_toCreate.save()
        module_json = ModuleSerializer(module_toCreate).data
        queryset = {}
        queryset['module'] = module_json
        queryset['message'] = "Module succesfully created for study group " +  studygroupJSON['studygroup_id']
        print(queryset)
        
        return Response(queryset)

class GetModule(APIView):
    def post(self, request, *args, **kwargs):
        def getContent(module):
            queryset = {}

            for entry in Material.objects.all().filter(module_id=module):
                entry_json = MaterialSerlizer(entry).data
                queryset[entry_json['material_id']] = entry_json

            return queryset

        queryset = {}

        module = Module.objects.get(module_id=request.data['module_id'])
        print(module)

        module_json = ModuleSerializer(module).data
        queryset = module_json
        queryset['content'] = getContent(module)
        account = Account.objects.get(id=module_json['module_owner'])
        account_json = AccountSerializer(account).data
        queryset['module_owner'] = account_json
        # for module in studygroup_modules:
        #     module_json = ModuleSerializer(module).data
        #     queryset[module_json['module_id']] = module_json
        #     queryset[module_json['module_id']]['content'] = getContent(module)

        #     account = Account.objects.get(id=module_json['module_owner'])
        #     account_json = AccountSerializer(account).data
        #     queryset[module_json['module_id']]['module_owner'] = account_json

        return Response(queryset)