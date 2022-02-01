from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer



from django.http import HttpResponse, JsonResponse
from .models import User, Organization
from .services import get_file_list, upload_file
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hi")


# def api(request):
#     return HttpResponse("list of api")

# ----------------------------------------------------------------------------


def filelists(request, uid):

    # current_user=User.objects.get(id=uid)
    #error catch for not exists user
    result= get_file_list(uid)
    return HttpResponse  ([ file.organization_files for file in result ])
    # return JsonResponse ({"Files are:": name.username for name in result })
    # return HttpResponse("this is the %s user." % current_user.username)

# @csrf_exempt
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
    # def uploadfile(uid):
    
    # if request=='POST':
        
    #     upload_file(request)
    # else:
    #     return False

