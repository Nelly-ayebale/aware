from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import User
from .forms import RegularUserSignUpForm, HospitalAdminstratorSignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

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
        kwargs['user_type'] = 'Regular User'
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





