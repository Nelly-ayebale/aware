from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import User,Hospital,Donor,BloodDrive
from .forms import RegularUserSignUpForm, HospitalAdminstratorSignUpForm,HospitalForm,BloodDriveForm,DonorForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    return render(request,'hospitals/home.html')

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class LoginView(TemplateView):
    template_name = 'registration/login.html'


class RegularUserSignUpView(CreateView):
    model = User
    form_class = RegularUserSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Donor'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class HospitalAdminstratorSignUpView(CreateView):
    model = User
    form_class = HospitalAdminstratorSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Adminstrator'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


@method_decorator([login_required, adminstrator_required], name='dispatch')
class HospitalCreateView(CreateView):
    model = Hospital
    fields = ('hospital_name','weight','capacity_required','capacity_available')
    template_name = hospitals/hospital.html

    def form_valid(self,form):
        hospital = form.save(commit=False)
        hospital.adminstrator = self.request.user
        hospital.save()
        messages.success(self.request,'Hospital created with success!')
        return redirect('home')

@method_decorator([login_required, regular_required], name='dispatch')
class DonorCreateView(CreateView):
    model = Donor
    fields = ('donor_name','donor_age','blood_type','blood_status','quantity_donated')
    template_name = hospitals/donor.html

    def form_valid(self,form):
        donor = form.save(commit=False)
        donor.donor = self.request.user
        donor.save()
        messages.success(self.request,'Thankyou,for saving a life today!')
        return redirect('home')

@method_decorator([login_required, adminstrator_required], name='dispatch')
class BloodDriveCreateView(CreateView):
    model = BloodDrive
    fields = ('drive_title','drive_location','drive_date','capacity_collected')
    template_name = hospitals/drive.html

    def form_valid(self,form):
        blooddrive = form.save(commit=False)
        blooddrive.drive_owner = self.request.user
        blooddrive.save()
        messages.success(self.request,'You successfully created a Blood Drive!')
        return redirect('home')




