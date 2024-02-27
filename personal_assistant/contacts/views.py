from datetime import date, timedelta
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from contacts.forms import ContactForm, UpcomingBirthdaysForm
from contacts.models import Contact
from user_auth.views import get_colleagues_ids, user_can_access


@login_required
def contact_list(request):
    colleagues_ids = get_colleagues_ids(request)
    contacts = Contact.objects.filter(created_by__in=colleagues_ids)
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


@login_required
def upcoming_birthdays(request):
    days = request.POST.get("days")
    form = UpcomingBirthdaysForm(request.POST)

    if not days:
        context = {"contacts": None, "form": form}
        return render(request, "contacts/upcoming_birthdays.html", context)

    days = int(days)

    today = date.today()

    # Filter for birthdays in the range
    conditions = []
    colleagues_ids = get_colleagues_ids(request)

    # Iterate over the range of days
    for delta in range(days):
        day_to_check = today + timedelta(days=delta)
        day_month_str = day_to_check.strftime("%m-%d")  # Format to 'MM-DD'

        # Using icontains to match the date format in the database
        conditions.append(Q(birthday__icontains=day_month_str))

    # Combine all conditions with OR
    query = conditions.pop()
    for condition in conditions:
        query |= condition

    # Query the database
    contacts = Contact.objects.filter(query, Q(created_by__in=colleagues_ids))

    context = {"contacts": contacts, "form": form}
    if not contacts:
        context["error_message"] = "No contacts found with upcoming birthdays."

    return render(request, "contacts/upcoming_birthdays.html", context)


@login_required
def create_or_edit_contact(request, contact_id=None):
    contact = get_object_or_404(Contact, pk=contact_id) if contact_id else None

    if not user_can_access(request.user, contact):
        return HttpResponseForbidden()

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            if (
                Contact.objects.filter(email=form.cleaned_data["email"])
                .exclude(pk=contact_id)
                .exists()
            ):
                messages.error(request, "Contact with this email already exists.")
            else:
                form.instance.modified_by = request.user
                if not form.instance.pk:
                    form.instance.created_by = request.user
                form.save()
                return redirect("contacts:contact_list")
        else:
            if "phone_number" in form.errors:
                messages.error(request, "Please enter correct phone number.")
            elif "email" in form.errors:
                messages.error(request, "Please enter correct email.")
    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        "contacts/create_or_edit_contact.html",
        {"form": form, "contact": contact},
    )


@login_required
def search_contacts(request):
    query = request.GET.get("q", "")
    contacts = []
    colleagues_ids = get_colleagues_ids(request)

    if query:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(address__icontains=query)
            | Q(phone_number__icontains=query)
            | Q(email__icontains=query),
            Q(created_by__in=colleagues_ids),
        )

        if not contacts:
            error_message = "No contacts found matching the search criteria."
            return render(
                request,
                "contacts/search_contacts.html",
                {"error_message": error_message, "query": query},
            )

    return render(
        request, "contacts/search_contacts.html", {"contacts": contacts, "query": query}
    )


@login_required
def delete_contact(request, contact_id):
    if not user_can_access(request.user, contact_id):
        return HttpResponseForbidden()
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect("contacts:contact_list")
