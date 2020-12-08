from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import User,BloodDrive,Hospital,Donor

class HospitalAdminstratorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user

class RegularUserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user

class BloodDriveForm(forms.ModelForm):
    class Meta:
        model = BloodDrive
        fields = ['drive_title','drive_location','drive_date','capacity_collected']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name','weight','capacity_required','capacity_available']

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['donor_name','donor_age','blood_type','blood_status','quantity_donated']

