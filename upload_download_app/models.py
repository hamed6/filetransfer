from django.db import models 

class Organization(models.Model):
    organization_name=models.CharField(max_length=10,blank=False)
    organization_files=models.FileField(upload_to='uploaded_files/')
    file_dlnumber=models.IntegerField(default=0)

class User(models.Model):
    username= models.CharField(max_length=20, blank=False)  
    organization_name=models.ForeignKey(Organization,on_delete=models.CASCADE, max_length=10, blank=False)