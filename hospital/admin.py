from django.contrib import admin
from .models import User,Hospital,Donor,BloodDrive
# Register your models here.
admin.site.register(User)
admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(BloodDrive)
