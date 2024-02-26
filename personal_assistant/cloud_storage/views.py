# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import FileForm
from .models import File
from .utils import get_file_extension, get_category_from_extension


# def upload(request):
#     context = {}
#     if request.method == "POST":
#         file = request.FILES["upload_file"]
#         fs = FileSystemStorage()
#         filename = fs.save(file.name, file)
#         url = fs.url(filename)
#         context["url"] = url
#     return render(request, "file_storage/upload.html", context)
# @login_required
# def upload(request):
#     form = FileForm()
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'File uploaded successfully')
#             return redirect('file_list')
#     else:
#         form = FileForm()
#     return render(request, 'cloud_storage/upload.html', {'form': form})

@login_required
def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user

            file_extension = get_file_extension(request.FILES['file'])
            file_instance.category = get_category_from_extension(file_extension)

            file_instance.save()
            messages.success(request, 'File uploaded successfully')
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'cloud_storage/upload.html', {'form': form})


@login_required
def file_list(request, category=None):
    user = request.user
    if not category:
        files = File.objects.filter(user=user).all()
    else:
        files = File.objects.filter(user=user, category=category).all()

    return render(request, 'cloud_storage/file_list.html', {'files': files})


def delete_file(request, file_id):
    if request.method == 'POST':
        file = File.objects.get(id=file_id)
        file.delete()
        messages.success(request, 'File deleted successfully')
    return redirect('file_list')
