from datetime import date, timedelta, timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from .forms import UpcomingBirthdaysForm
from django.db.models import Q
from datetime import timedelta


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def upcoming_birthdays(request, days=7):
    today = date.today()
    end_date = today + timedelta(days=int(days))
    contacts = Contact.objects.filter(birthday__range=[today, end_date])

    form = UpcomingBirthdaysForm()

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
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/create_or_edit_contact.html', {'form': form, 'contact': contact})

def search_contacts(request):
    query = request.GET.get('q', '')

    if query:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        contacts = Contact.objects.all()

    if not contacts:
        error_message = "No contacts found matching the search criteria."
        return render(request, 'contacts/search_contacts.html', {'error_message': error_message})

    return render(request, 'contacts/search_contacts.html', {'contacts': contacts, 'query': query})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('contact_list')