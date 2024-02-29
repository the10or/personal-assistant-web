from django import forms

from .models import Note, Tag

form_style = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": form_style}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": form_style}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": form_style}),
    )

    class Meta:
        model = Note
        fields = ["title", "content", "tags"]

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields["tags"].required = False


class TagForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": form_style}))

    class Meta:
        model = Tag
        fields = ["name"]
