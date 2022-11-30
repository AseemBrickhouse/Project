from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from backend.AllViews.Util.MaterialUtil import *
import random
import string

class CreateMaterial(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.data['token']).user_id
        currentUser = User.objects.all().filter(id=token)[0].account

        module_obj = None
        try:
            module_obj = Module.objects.get(module_id=request.data['module_id'])
        except Module.DoesNotExist:
            module_obj = None

        print(getDir(module_obj.studygroup_id.studygroup_id))
        material = Material.objects.create(
            material_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
            material_type = request.data['type'],
            account = currentUser,
            module_id = module_obj,
            content = request.data['content'],
            # file_content_upload = 
        )

        material.save()

        return Response({
            "Message": "Material succesfully created"
        })
        
class GetModuleMaterial(APIView):
    def post(self, request, *args, **kwargs):
        # material = Material.objects.all().filter(module_id=request.data['module_id'])
        queryset = {}
        module = Module.objects.all().get(module_id=request.data['module_id'])
        module_json = ModuleSerializer(module).data
        for material in Material.objects.all().filter(module_id=module):
            material_json = MaterialSerlizer(material).data
            queryset[material_json['material_id']] = material_json

        return Response(queryset)

class DeleteMaterial(APIView):
    def delete(self, request, *args, **kwargs):
        pass

class UpdateMaterial(APIView):
    def put(self, request, *args, **kwargs):
        pass