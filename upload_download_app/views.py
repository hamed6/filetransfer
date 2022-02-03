from django.http import FileResponse, HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization, User
from .serializers import FileSerializer, StatisticsSerializer
from .services import find_org


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


# The idea was to use ViewSet and Serializer otherwise, 
# it would be possble to get all objects from Organization 
# and then Organization.organization_files.name.
class FileTrasnferView(viewsets.ViewSet):
    serializer_class= FileSerializer
    def list(self, request):
        queryset= Organization.objects.all()
        serializer= FileSerializer(queryset, many=True)
        return Response ( serializer.data)


def downloadfilefromdb(request,fileid):
    fileobj=Organization.objects.get(id=fileid)
    fileobj.file_dlnumber+=1
    fileobj.save()
    fileaddress=fileobj.organization_files.path
    dlfile=FileResponse(open(fileaddress, 'rb'))
    return dlfile



# Group all similar Organization names + file_dlnumber fields
#  will give: The total file downloads each organization
class NumberOfDownload(generics.ListCreateAPIView):
    serializer_class = StatisticsSerializer
    queryset= Organization.objects.all()
    def list(self, request):
        queryset=self.get_queryset()
        serializer=StatisticsSerializer(queryset, many=True)
        return Response(serializer.data)



# ===============================================================================


# Class to view the list of users if it's needed.
class UsersList(APIView):
    def get(self,request):
        users=[user.username for user in User.objects.all()]
        return Response(users)

# To give a basic view from the home page
def index(request):
    return HttpResponse("The placeholder for the homepage")

