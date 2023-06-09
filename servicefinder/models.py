from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userdetail(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=13)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return "username "+str(self.username)+" Phone "+self.phone

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=13)
    message=models.TextField()

    
    def __str__(self):
        return "sno "+str(self.sno)+" msg "+self.message[:20]


class Partner(models.Model):
    sno=models.AutoField(primary_key=True)
    profile_img=models.ImageField(upload_to='media/profile',default='')
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    address=models.CharField(max_length=100,default='')
    aadhar=models.IntegerField()
    city=models.CharField(max_length=40,default='')
    service=models.CharField(max_length=50)
    timing=models.CharField(max_length=50,default='')
    fee=models.IntegerField()

class PartnerProfile(models.Model):
    sno=models.AutoField(primary_key=True)
    userid=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    profile_img=models.ImageField(upload_to='media/profile',default='')
    aadhar=models.IntegerField()
    address=models.CharField(max_length=100,default='')
    status=models.BooleanField(default=True)

class PartnerService(models.Model):
    sno=models.AutoField(primary_key=True)
    profile=models.ForeignKey(PartnerProfile,on_delete=models.CASCADE)
    service=models.CharField(max_length=50)
    city=models.CharField(max_length=40)
    timing=models.CharField(max_length=50)
    fee=models.IntegerField()
    userstatus=models.BooleanField(default=True)
    status=models.BooleanField(default=False)








class Booking(models.Model):
    sno=models.AutoField(primary_key=True)
    userid=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    servicer=models.ForeignKey(PartnerService,on_delete=models.CASCADE)
    mapurl=models.CharField(max_length=200,default='')
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    bookingdate=models.DateField(auto_now_add=True)
    bookingtime=models.TimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=False)
    f_time=models.TimeField(auto_now_add=False)
    a_time=models.TimeField(auto_now_add=False)
    description=models.TextField()
    status=models.CharField(max_length=20,default='')


class PartnerBookings(models.Model):
    sno=models.AutoField(primary_key=True)
    p_username=models.CharField(max_length=50)
    Booking_details=models.ForeignKey(Booking,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)
    confirm=models.BooleanField(default=False)
