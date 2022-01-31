from django.http import JsonResponse
from .models import Organization, User

# get_file_list
# upload_file
# get_dl_number_file
# get_dl_number_org


def get_file_list(uid):
   user=User.objects.get(id=uid)
   org_files=User.objects.all().filter(organization_name=user.organization_name)
   return (org_files)
#    org_files=Organization.objects.all().filter(organization_name=user.organization_name)
   