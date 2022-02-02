# from django.db import router
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import  UploadFile, UserUploadFile
from .routers import router

urlpatterns=[
    path('',views.index, name='index'),
    path('api/upload/<str:uid>', UserUploadFile.as_view(), name="upload"),
    path('api/viewfilelist/', include(router.urls) , name="users"),
    
    # path('uploads/',UploadFile.as_view(), name='fileupload)'),
]


# /api/upload/uid/'uploadfile' : post/put
# /api/viewfilelist/uid : GET
# /api/download/uid/filenumber: add +1 to dl column of file GET

# /api/filestatistic: list of file with number of dl in front of that GET
# /api/orgstatistic: list of org with number of dl in front of it GET