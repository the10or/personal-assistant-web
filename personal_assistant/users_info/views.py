from django.shortcuts import redirect, render
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from user_auth.models import User
from .forms import UserDescriptionForm


@login_required
def contact_list(request):
    user = request.user
    contacts = Contact.objects.filter(created_by=user.id).order_by('-id')[:10]

    # user = User
    # print(user) 
    return render(request, 'users_info/dashboard.html', {'contacts': contacts, 'user': user})


@login_required
def create_description(request):
    if request.method == 'POST':
        form = UserDescriptionForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
    else:
        form = UserDescriptionForm()
    return render(request, 'users_info/edit_user.html', {'form': form})
