from django import forms
from django.core.validators import RegexValidator

from .models import Contact


class ContactForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Enter a valid phone number.',
    )

    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message='Enter a valid email address.',
    )

    phone_number = forms.CharField(validators=[phone_validator], max_length=15)
    email = forms.EmailField(validators=[email_validator])

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email', 'birthday']


class UpcomingBirthdaysForm(forms.Form):
    days = forms.IntegerField(label='Enter the number of days', initial=7, required=False, min_value=1)
