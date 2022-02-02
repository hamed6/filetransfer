from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import FileSerializer
from django.http import HttpResponse, JsonResponse
from .models import User, Organization
from .services import get_file_list, upload_file, find_org


class UserUploadFile(APIView):
    def post(self, request,uid):
        try:
            orgobj=Organization()
            orgobj.organization_name=find_org(uid)
            orgobj.organization_files=request.data.get('organization_files')
            orgobj.save()
            return Response('File uploaded successfully!', status=status.HTTP_201_CREATED)
        except AttributeError:
            return Response('Wrong input!', status=status.HTTP_400_BAD_REQUEST)




class FileTrasnferView(viewsets.ViewSet):
    serializer_class= FileSerializer
    def list(self, request):
        queryset= Organization.objects.all()
        serializer= FileSerializer(queryset, many=True)
        return Response ( serializer.data)




# ===============================================================================



# Endpoint to view the list of users if needed.
class UsersList(APIView):
    def get(self,request):
        users=[user.username for user in User.objects.all()]
        return Response(users)






















def index(request):
    return HttpResponse("The placeholder for the homepage")

# ----------------------------------------------------------------------------


def filelists(request, uid):

    # current_user=User.objects.get(id=uid)
    #error catch for not exists user
    result= get_file_list(uid)
    return HttpResponse  ([ file.organization_files for file in result ])
    # return JsonResponse ({"Files are:": name.username for name in result })
    # return HttpResponse("this is the %s user." % current_user.username)




        
class UploadFile(APIView):
    parser_class={MultiPartParser, FormParser}

    def post(self, request, *args, **kwargs):
        file_serializer=FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
            status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


