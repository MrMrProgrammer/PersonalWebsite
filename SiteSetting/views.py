from django.shortcuts import render
from .models import HomeData


# Create your views here.

def Home(request):

    home_data = HomeData.objects.filter(is_active=True).last()

    context = {
        'home_data': home_data
    }

    return render(request, 'SiteSetting/index.html', context)


def Resume(request):
    return render(request, 'SiteSetting/resume.html')



