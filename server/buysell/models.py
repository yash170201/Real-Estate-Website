from distutils.command.upload import upload
from django.db import models
from django.core.files.storage import FileSystemStorage

class Buysell(models.Model):
    Username=models.CharField(max_length=20)
    name = models.CharField( max_length=24)
    email = models.EmailField()
    Password=models.CharField(max_length=20)
    Age=models.CharField(max_length=4,default=0)
    Phone=models.CharField(max_length=10,default=0)   

class LegalAdvisor(models.Model):
    Username=models.CharField(max_length=20)
    name = models.CharField(max_length=24)
    email = models.EmailField()
    Password=models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    License=models.CharField(max_length=20)
    # fs=FileSystemStorage()
    File = models.FileField(upload_to='upload') 
    file_url=models.URLField(default=0)
    Profile=models.FileField(upload_to='upload')
    profile_url=models.URLField(default=0)



# class City(models.Model):
#     city=models.CharField(max_length=30)
#     properties=models.ForeignKey(Addproperty)

class Addproperty(models.Model):
    # name=models.CharField(max_length=30)
    # email = models.EmailField(default=0)
    # postal=models.IntegerField()
    # address=models.CharField(max_length=255)
    # phone=models.CharField(max_length=20)
    # price=models.IntegerField()
    # size=models.IntegerField()
    # des=models.CharField(max_length=255)
    # city=models.CharField(max_length=20)
    # File=models.ImageField(upload_to='upload')
    # File_url=models.URLField()
    Property=models.JSONField(null=True)
    
    # def __str__(self):
    #     return self.name

