from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Experience, Skill, Project, Certification, Education

def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()[:3]
    context = {
        'profile': profile,
        'featured_projects': projects,
    }
    return render(request, 'main/index.html', context)

def about(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    context = {
        'profile': profile,
        'education': education,
    }
    return render(request, 'main/about.html', context)

def skills(request):
    skills = Skill.objects.all()
    categories = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(skill)
    
    context = {
        'skills': skills,
        'skill_categories': categories,
    }
    return render(request, 'main/skills.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'main/projects.html', context)

def experience(request):
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences,
    }
    return render(request, 'main/experience.html', context)

def achievements(request):
    certifications = Certification.objects.all()
    context = {
        'certifications': certifications,
    }
    return render(request, 'main/achievements.html', context)

def resume(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'skills': skills,
        'education': education,
        'certifications': certifications,
    }
    return render(request, 'main/resume.html', context)

def contact(request):
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        if name and email and subject and message:
            # For now, just return success (email sending requires proper SMTP configuration)
            # You can add email functionality later by configuring EMAIL settings in settings.py
            return JsonResponse({
                'success': True,
                'message': f'Thank you {name}! Your message has been received. I will get back to you at {email} soon.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all fields.'
            })
    
    context = {
        'profile': profile,
    }
    return render(request, 'main/contact.html', context)
