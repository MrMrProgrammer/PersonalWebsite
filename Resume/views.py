from django.shortcuts import render
from .models import Skill, Language, Experience


def Resume(request):
    skills = Skill.objects.filter(is_active=True).order_by('-priority')
    languages = Language.objects.filter(is_active=True).order_by('-priority')
    experiences = Experience.objects.filter(is_active=True).order_by('-priority')

    context = {
        'skills': skills,
        'languages': languages,
        'experiences': experiences,
    }

    return render(request, 'Resume/resume.html', context)
