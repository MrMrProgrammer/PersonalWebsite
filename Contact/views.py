from django.shortcuts import render, redirect
from .forms import ContactForm


def get_message(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = ContactForm()

    return render(request, 'SiteSetting/templates/Contact/contact.html', {'form': form})


def Contact(request):
    return render(request, 'SiteSetting/../Contact/templates/Contact/contact.html')
