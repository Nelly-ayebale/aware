from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView,ListView
from .models import User,Hospital,Donor,Drive
from .forms import RegularUserSignUpForm, HospitalAdminstratorSignUpForm,HospitalForm,BloodDriveForm,DonorForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .decorators import adminstrator_required,regular_required
from .forms import SubscriptionForm
from django.http import JsonResponse

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

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
        return redirect('drive')

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
        return redirect('drive')

@method_decorator([login_required, adminstrator_required], name='dispatch')
class HospitalCreateView(CreateView):
    model = Hospital
    fields = ('hospital_name','capacity_required','capacity_available')
    template_name = 'hospitals/hospital.html'

    def form_valid(self,form):
        hospital = form.save(commit=False)
        hospital.adminstrator = self.request.user
        hospital.save()
        messages.success(self.request,'Hospital created with success!')
        return redirect('drive')

@method_decorator([login_required, regular_required], name='dispatch')
class DonorCreateView(CreateView):
    model = Donor
    fields = ('donor_first_name','donor_last_name','donor_age','blood_type','blood_status','weight','quantity_donated')
    template_name = 'hospitals/donor.html'

    def form_valid(self,form):
        donor = form.save(commit=False)
        donor.donor = self.request.user
        donor.save()
        messages.success(self.request,'Thankyou,for saving a life today!')
        return redirect('drive')

@method_decorator([login_required, adminstrator_required], name='dispatch')
class DriveCreateView(CreateView):
    model = Drive
    fields = ('drive_title','drive_location','photo','comment','capacity_collected')
    template_name = 'hospitals/drive.html'

    def form_valid(self,form):
        blooddrive = form.save(commit=False)
        blooddrive.drive_owner = self.request.user
        blooddrive.save()
        messages.success(self.request,'You successfully created a Blood Drive!')
        return redirect('drive')

@login_required(login_url='login')
def all_hospitals(request):
    hospitals = Hospital.objects.all()
    
    return render(request,'hospitals/hospital_list.html',{"hospitals":hospitals})


@method_decorator([login_required, adminstrator_required], name='dispatch')
class ViewDonorsList(ListView):
    queryset = Donor.objects.all()
    template_name = 'hospitals/donor_list.html'

@login_required(login_url='login')
def drives(request):
    drives = Drive.objects.all()
    
    return render(request,'hospitals/drives.html',{"drives":drives})

def search_results(request):

    if 'hospital' in request.GET and request.GET["hospital"]:
        search_term = request.GET.get("hospital")
        searched_hospitals = Hospital.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'hospitals/search.html',{"message":message,"hospitals": searched_hospitals})

    else:
        message = "You haven't searched for any term"
        return render(request, 'hospitals/search.html',{"message":message})

@login_required(login_url='login')
def single_hospital(request,hospital_id):
    form = SubscriptionForm()
    try:
        hospital = Hospital.objects.get(id = hospital_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"hospitals/single_hospital.html", {"hospital":hospital,"letterForm":form})


def subscription(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = SubscriptionRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to our mailing list'}
    return JsonResponse(data)