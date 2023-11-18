from django.shortcuts import render


def Resume(request):
    return render(request, 'Resume/resume.html')