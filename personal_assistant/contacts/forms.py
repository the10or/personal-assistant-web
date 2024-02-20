from django import forms
from django.core.validators import RegexValidator

from .models import Contact

form_style = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class ContactForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Enter a valid phone number.',
    )

    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message='Enter a valid email address.',
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': form_style}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': form_style}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': form_style}))
    phone_number = forms.CharField(validators=[phone_validator], max_length=15, widget=forms.TextInput(attrs={'class': form_style}))
    email = forms.EmailField(validators=[email_validator], widget=forms.TextInput(attrs={'class': form_style}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'class': form_style, "type": "date"}))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'birthday', 'address']


class UpcomingBirthdaysForm(forms.Form):
    days = forms.IntegerField(label='Enter the number of days', initial=7, required=False, min_value=1, widget=forms.NumberInput(attrs={'class': form_style}))
