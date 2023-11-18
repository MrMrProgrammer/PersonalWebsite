from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name...',
            'id': 'name'
        })
    )

    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com',
            'id': 'email',
        })
    )

    phone_number = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(123) 456-7890',
            'id': "phone",
        })
    )

    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message here...',
            'id': "message",
            "rows": "10",
        })
    )

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'message']
