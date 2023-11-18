from django.shortcuts import render, redirect
from .forms import ContactForm


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = ContactForm()

        context = {
            'form': form,
        }

    return render(request, 'Contact/contact.html', context)
