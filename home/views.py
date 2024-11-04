from django.shortcuts import render
from .models import About, Education, Experience, Skill, Certificate
from django.http import FileResponse, Http404
import os

def home(request):
    context = {
        'about': About.objects.first(),
        'educations': Education.objects.all().order_by('-end_date'),
        'experiences': Experience.objects.all().order_by('-years_of_experience'),
        'skills': Skill.objects.all(),
        'certificates': Certificate.objects.all().order_by('-date')
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def skills(request):
    return render(request, 'home/skills.html')

def experience(request):
    return render(request, 'home/experience.html')

def education(request):
    return render(request, 'home/education.html')

def certificate(request):
    return render(request, 'home/certificate.html')

def project(request):
    return render(request, 'home/project.html')

def download_pdf(request):
    about = About.objects.first()
    if about and about.resume_pdf:
        try:
            return FileResponse(about.resume_pdf, content_type='application/pdf')
        except FileNotFoundError:
            raise Http404("PDF bulunamadı")
    raise Http404("PDF yüklenmemiş")
