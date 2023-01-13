from django.db import models

# Create your models here.
class register(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Status = models.BooleanField(default=False)

class fileupload(models.Model):
    Name = models.CharField(max_length=20)
    Designation = models.CharField(max_length=20)
    File = models.FileField()