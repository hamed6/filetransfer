from django.http import Http404, HttpResponse
from .models import Organization, User


def find_org(uid):
    user_organization=User.objects.get(id=uid)
    return user_organization.organization_name


