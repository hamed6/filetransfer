from django.db import models 

oraganzation_catgory=[
        ('SL','Sales'),
        ('MK','Marketing'),
        ('RD', 'Research And Develop'),
        ('IT','Information Technology'),
        ]

class User(models.Model):
    
    username= models.CharField(max_length=20, blank=False)  
    organization_name=models.CharField(choices=oraganzation_catgory, max_length=25)    

    def __str__(self):
        return self.username

class Organization(models.Model):
    
    organization_name=models.CharField(choices=oraganzation_catgory, max_length=25)    
    # organization_name=models.ForeignKey(User,on_delete=models.CASCADE, max_length=25, blank=False)    
    # organization_name=models.CharField(max_length=10,blank=False)
    organization_files=models.FileField(upload_to='uploaded_files/')
    file_dlnumber=models.IntegerField(default=0)

    def __str__(self):
        return self.organization_name
