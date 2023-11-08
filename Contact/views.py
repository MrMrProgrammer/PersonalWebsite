from django.shortcuts import render, redirect
from django.views import View

from .forms import ContactForm


# Create your views here.


def get_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = ContactForm()

    return render(request, 'SiteSetting/contact.html', {'form': form})
