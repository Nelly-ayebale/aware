from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('adminstrator status',default=False)
    is_user = models.BooleanField('regular status', default=False)

