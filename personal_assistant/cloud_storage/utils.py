# utils.py

from django.utils.text import get_valid_filename
import os

def get_file_extension(file):
    filename, file_extension = os.path.splitext(file.name)
    return file_extension.lower()

def get_category_from_extension(file_extension):
    if file_extension in ['.pdf', '.doc', '.docx', '.txt']:
        return 'documents'
    elif file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
        return 'videos'
    elif file_extension in ['.mp3', '.wav', '.flac']:
        return 'audio'
    elif file_extension in ['.jpg', '.png', '.gif', '.bmp']:
        return 'images'
    else:
        return 'other'