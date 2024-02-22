from datetime import date, timedelta
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactForm
from .forms import UpcomingBirthdaysForm
from .models import Contact
from django.http import HttpResponseNotFound


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def upcoming_birthdays(request):
    days = request.POST.get('days')
    form = UpcomingBirthdaysForm(request.POST)

    if not days:
        context = {'contacts': None, 'form': form}
        return render(request, 'contacts/upcoming_birthdays.html', context)
    
    days = int(days)
    
    today = date.today()

    # Filter for birthdays in the range
    conditions = []

    # Iterate over the range of days
    for delta in range(days):
        day_to_check = today + timedelta(days=delta)
        day_month_str = day_to_check.strftime("%m-%d")  # Format to 'MM-DD'

        # Using icontains to match the date format in the database
        conditions.append(
            Q(birthday__icontains=day_month_str)
        )

    # Combine all conditions with OR
    query = conditions.pop()
    for condition in conditions:
        query |= condition

    # Query the database
    contacts = Contact.objects.filter(query)


    context = {'contacts': contacts, 'form': form}
    if not contacts:
        context['error_message'] = "No contacts found with upcoming birthdays."

    return render(request, 'contacts/upcoming_birthdays.html', context)


def create_or_edit_contact(request, contact_id=None):
    contact = get_object_or_404(Contact, pk=contact_id) if contact_id else None

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
        elif form.has_error('phone_number'):
            messages.error(request, 'Please enter correct phone number.')
        elif form.has_error('email'):
            messages.error(request, 'Please enter correct email.')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/create_or_edit_contact.html', {'form': form, 'contact': contact})

def search_contacts(request):
    query = request.GET.get('q', '')
    contacts = []

    if query:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query)
        )

        if not contacts:
            error_message = "No contacts found matching the search criteria."
            return render(request, 'contacts/search_contacts.html', {'error_message': error_message, 'query': query})

    return render(request, 'contacts/search_contacts.html', {'contacts': contacts, 'query': query})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('contacts:contact_list')
