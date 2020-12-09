from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import User,Drive,Hospital,Donor

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
        model = Drive
        fields = ['drive_title','drive_location','capacity_collected']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name','capacity_required','capacity_available']

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['donor_first_name','donor_last_name','donor_age','blood_type','blood_status','weight','quantity_donated']

