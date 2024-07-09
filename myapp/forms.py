from django import forms
from django.forms import ModelForm
from . models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
        }
        help_texts = {
            'name': 'Please enter your full name.',
            'email': 'Please enter a valid email address.',
        }
        error_messages = {
            'name': {
                'max_length': 'Name should not exceed 100 characters.',
            },
            'email': {
            'unique': 'This email address is already registered.',
            },
            'required': 'This field is required.',
            'invalid': 'Please enter a valid email address.',
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        # }

