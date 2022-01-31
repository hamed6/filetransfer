from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('api/<str:uid>',views.filelists, name='filelists'),
]