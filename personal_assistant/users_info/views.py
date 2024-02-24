from django.shortcuts import redirect, render
from contacts.models import Contact
from .decorators import user_not_authenticated
from .models import User
from .forms import UserDescriptionForm  


@user_not_authenticated
def contact_list(request):
    user = request.user
    contacts = Contact.objects.filter(created_by=user.id).order_by('-id')[:10]

    # user = User
    # print(user) 
    return render(request, 'users_info/dashboard.html', {'contacts': contacts, 'user' : user})


@user_not_authenticated
def create_description(request):
    if request.method == 'POST':
        form = UserDescriptionForm(request.POST)
        if form.is_valid():
            user = request.user
            user.description = form.cleaned_data['description']
            user.save()

    else:
        form = UserDescriptionForm()

    return render(request, 'users_info/dashboard.html', {'form': form})
