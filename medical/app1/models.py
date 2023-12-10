from django.db import models

# Create your models here.
class RegModel(models.Model):

    fname=models.CharField(max_length=250,blank=True)
    lname=models.CharField(max_length=250,blank=True)
    propic=models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    uname=models.CharField(max_length=250,blank=True)
    email=models.EmailField(max_length=250,null=True,unique=True)
    psw=models.CharField(max_length=250,blank=True)
    utype=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.fname

class Address(models.Model):
    user = models.OneToOneField(RegModel, on_delete=models.CASCADE)
    line = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=255,blank=True)
    state = models.CharField(max_length=255,blank=True)
    pincode = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return str(self.user)
