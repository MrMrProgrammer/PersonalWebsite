from django.shortcuts import render
from .models import Project


def Projects(request):
    projects = Project.objects.filter(is_active=True)

    context = {
        'projects': projects,
    }

    return render(request, 'Project/projects.html', context)
