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