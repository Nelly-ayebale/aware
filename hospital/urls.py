from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    path('hospital/add/', views.HospitalCreateView.as_view(), name='hospital'),
    path('donor/',views.DonorCreateView.as_view(),name='donor'),
    path('',views.DriveCreateView.as_view(),name='home'),
    path('hospitals/',views.ViewHospitalsList.as_view(),name='view_hospitals'),
    path('all_donors/',views.ViewDonorsList.as_view(),name='view_donors'),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

