from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from user_auth.views import get_colleagues_ids, user_can_access

from .forms import NoteForm, TagForm
from .models import Note, Tag


@login_required
def note_list(request):
    colleagues_ids = get_colleagues_ids(request)
    notes = Note.objects.filter(created_by__in=colleagues_ids)
    tags = Tag.objects.all()

    tag_filter = request.GET.get("tag_filter")
    if tag_filter:
        notes = notes.filter(tags__name=tag_filter)

    sort_by_tag = request.GET.get("sort_by_tag")
    if sort_by_tag:
        notes = notes.order_by("tags__name")

    return render(request, "notes/note_list.html", {"notes": notes, "tags": tags})


@login_required
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            form.save_m2m()
            return redirect("notes:note_list")
    else:
        form = NoteForm()
    return render(
        request, "notes/add_note.html", {"form": form, "tags": Tag.objects.all()}
    )


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if not user_can_access(request.user, note):
        return HttpResponseForbidden()
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.modified_by = request.user
            note.save()
            form.save_m2m()
            return redirect("notes:note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/edit_note.html", {"form": form, "note": note})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if not user_can_access(request.user, note):
        return HttpResponseForbidden()
    note.delete()
    return redirect("notes:note_list")


@login_required
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data["name"]
            if Tag.objects.filter(name=tag_name).exists():
                messages.error(request, "Tag already exists")
            else:
                form.save()
                messages.success(request, "Tag added successfully")
                return HttpResponseRedirect(
                    reverse("notes:note_list") + "?message=Tag added successfully"
                )
    else:
        form = TagForm()
    return render(request, "notes/add_tag.html", {"form": form})


@login_required
def details_note(request, note_id):
    note = Note.objects.filter(
        id=note_id, created_by__in=get_colleagues_ids(request)
    ).first()
    return render(request, "notes/note_details.html", {"note": note})
