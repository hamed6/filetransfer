from django.urls import path
from django.conf.urls import url
from . import views
from .views import UploadFile

urlpatterns=[
    path('',views.index, name='index'),
    path('api/<str:uid>',views.filelists, name='filelists'),
    # path('api/upload/<str:uid>', views.UploadFile, name='uploadfile')
    url('upload/',UploadFile, name='fileupload)')
]


# /api/upload/uid/'uploadfile'
# /api/viewfilelist/uid
# /api/download/uid/filenumber: add +1 to dl column of file

# /api/filestatistic: list of file with number of dl in front of that
# /api/orgstatistic: list of org with number of dl in front of it