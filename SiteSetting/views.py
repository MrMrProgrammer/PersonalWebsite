from django.shortcuts import render
from .models import HomeData
from Log.loggers import saveLog


# Create your views here.

def Home(request):
    try:
        # --------------
        saveLog(request)
        # --------------
    except:
        pass

    home_data = HomeData.objects.filter(is_active=True).last()

    context = {
        'home_data': home_data
    }

    return render(request, 'SiteSetting/index.html', context)
