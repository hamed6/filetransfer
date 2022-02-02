from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer


from django.http import Http404, HttpResponse
from .models import Organization, User


def find_org(uid):
    user_organization=User.objects.get(id=uid)
    return user_organization.organization_name



#=================================================================
def find_user(uid):
    user=User.objects.get(id=uid)
    return user



def get_file_list(uid):
    try:
        # user=find_user(uid)
        org=find_org(uid)
    except User.DoesNotExist:
        raise Http404("User is not valid!")
    return (org)
#    org_files=Organization.objects.all().filter(organization_name=user.organization_name)
   


def upload_file(request):
    # // counter field is required
    
    org=Organization (organization_name = request.organization_name , organization_files = request.organization_files , file_dlnumber=+1)
    org.save()    
    return HttpResponse("file saved!")