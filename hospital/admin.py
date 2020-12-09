from django.contrib import admin
from .models import User,Hospital,Donor,Drive
# Register your models here.
admin.site.register(User)
admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(Drive)
