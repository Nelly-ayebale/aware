from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.drives,name='drive'),
    path('hospital/add/', views.HospitalCreateView.as_view(), name='hospital'),
    path('donor/',views.DonorCreateView.as_view(),name='donor'),
    path('create_drives/',views.DriveCreateView.as_view(),name='create_drives'),
    path('hospitals/',views.all_hospitals,name='view_hospitals'),
    path('all_donors/',views.ViewDonorsList.as_view(),name='view_donors'),
    path('search/', views.search_results, name='search_results'),
    path('hospital/<int:hospital_id>',views.single_hospital,name ='single_hospital'),
    path('ajax/subscriptionletter/', views.subscription, name='subscriptionletter')
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

