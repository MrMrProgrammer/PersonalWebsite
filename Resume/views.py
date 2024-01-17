from django.shortcuts import render
from .models import Skill, Language, Experience, Education, ResumeFile


def Resume(request):
    skills = Skill.objects.filter(is_active=True).order_by('-priority')
    languages = Language.objects.filter(is_active=True).order_by('-priority')
    experiences = Experience.objects.filter(is_active=True).order_by('-priority')
    educations = Education.objects.filter(is_active=True).order_by('-id')
    resume_file = ResumeFile.objects.filter(is_active=True).last()

    context = {
        'skills': skills,
        'languages': languages,
        'experiences': experiences,
        'educations': educations,
        'resume_file': resume_file,
    }

    return render(request, 'Resume/resume.html', context)
