from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import   UserUploadFile, NumberOfDownload
from .routers import router

urlpatterns=[
    path('',views.index, name='index'),
    path('api/upload/<str:uid>', UserUploadFile.as_view(), name="upload"),
    path('api/viewfilelist/', include(router.urls) , name="users"),
    path('api/download/<str:fileid>', views.downloadfilefromdb, name="download"),
    path('api/filestatistic', NumberOfDownload.as_view(), name="filestatistics"),
]
