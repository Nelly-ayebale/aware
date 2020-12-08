from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('adminstrator status',default=False)
    is_user = models.BooleanField('regular status', default=False)

class Hospital(models.Model):
    adminstrator = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    hospital_name = models.CharField(max_length=400)
    capacity_required = models.IntegerField(default=0)
    capacity_available = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Donor(models.Model):
    donor = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image',blank=True,null=True)
    donor_name = models.CharField(max_length=200)
    donor_age = models.IntegerField(default=0)
    blood_type = models.CharField(max_length=5)
    blood_status = models.TextField(max_length=60)
    quantity_donated = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class BloodDrive(models.Model):
    drive_owner = models.ForeignKey('Hospital',on_delete=models.CASCADE)
    drive_title = models.CharField(max_length=150)
    drive_location = models.TextField(max_length=255)
    drive_date = models.DateTimeField(auto_now_add=True)
    capacity_collected = models.IntegerField(default=0)
    donors = models.ForeignKey('Donor',on_delete=models.CASCADE)

    def __str__(self):
        return self.drive_title