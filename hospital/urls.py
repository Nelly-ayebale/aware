from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('hospital/add/', views.HospitalCreateView.as_view(), name='hospital'),
    path('donor/',views.DonorCreateView.as_view(),name='donor'),
    path('drive/',views.BloodDriveCreateView.as_view(),name='drive'),
    path('hospitals/',views.ViewHospitalsList.as_view(),name='view_hospitals')
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

