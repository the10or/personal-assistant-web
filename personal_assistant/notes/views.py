from django.shortcuts import render, get_object_or_404, redirect
from pydantic import Tag
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note,Tag
from .forms import NoteForm

@login_required
def note_list(request):
    notes = Note.objects.filter(created_by=request.user)
    tags = Tag.objects.all()

    tag_filter = request.GET.get('tag_filter')
    if tag_filter:
        notes = notes.filter(tags__name=tag_filter)

    sort_by_tag = request.GET.get('sort_by_tag')
    if sort_by_tag:
        notes = notes.order_by('tags__name')

    return render(request, 'notes/note_list.html', {'notes': notes, 'tags': tags})


@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            form.save_m2m()  
            return redirect('notes:note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form, 'tags': Tag.objects.all()})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.modified_by = request.user
            note.save()
            form.save_m2m()  
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('notes:note_list')
