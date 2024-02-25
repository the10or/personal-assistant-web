from django import forms
from user_auth.models import User

form_style = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class UserDescriptionForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': form_style}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': form_style}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': form_style}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
