from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('adminstrator status',default=False)
    is_user = models.BooleanField('regular status', default=False)

class BloodDrives(models.Model):
    hospital_name = models.CharField(max_length=200)
    drive_location = models.TextField(max_length=400)
    drive_date = models.DateTimeField(auto_now_add=True)