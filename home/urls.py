from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('certificate/', views.certificate, name='certificate'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]