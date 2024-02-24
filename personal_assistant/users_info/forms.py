from django import forms
from .models import User

class UserDescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['description']
