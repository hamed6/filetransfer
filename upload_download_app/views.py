from django.http import HttpResponse, JsonResponse
from .models import User, Organization
from .services import get_file_list

def index(request):
    return HttpResponse("Hi")


# def api(request):
#     return HttpResponse("list of api")

# ----------------------------------------------------------------------------




def filelists(request, uid):

    # current_user=User.objects.get(id=uid)
    #error catch for not exists user
    result= get_file_list(uid)
    return HttpResponse  ([ name.username for name in result ])
    # return JsonResponse ({"Files are:": name.username for name in result })
    # return HttpResponse("this is the %s user." % current_user.username)



