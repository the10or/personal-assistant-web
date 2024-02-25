from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users_info.forms import EditFirstNameForm, EditLastNameForm, EditEmailForm

@login_required
def contact_list(request):
    user = request.user
    contacts = Contact.objects.filter(created_by=user.id).order_by('-id')[:10]

    # user = User
    # print(user) 
    return render(request, 'users_info/dashboard.html', {'contacts': contacts, 'user': user})


@login_required
def edit_first_name(request):
    if request.method == 'POST':
        form = request.POST
        user = request.user
        user.first_name = form['first_name']
        user.save()
    else:
        form = EditFirstNameForm()
    return render(request, 'users_info/edit_first_name.html', {'form': form})


@login_required
def edit_last_name(request):
    if request.method == 'POST':
        form = request.POST
        user = request.user
        user.last_name = form['last_name']
        user.save()
    else:
        form = EditLastNameForm()
    return render(request, 'users_info/edit_last_name.html', {'form': form})


@login_required
def edit_email(request):
    if request.method == 'POST':
        form = request.POST
        user = request.user
        user.email = form['email']
        user.save()
    else:
        form = EditEmailForm()
    return render(request, 'users_info/edit_email.html', {'form': form})
