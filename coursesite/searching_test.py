import os
import sys
import django

# Add the path to your Django project's settings module
sys.path.append('C:/Users/mariy/PycharmProjects/coursesite')

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'coursesite.settings'

# Initialize Django
django.setup()

# Import the Book model after initializing Django
from courseapp.models import Book

# Code for executing the script
name_of_book = 'antena'
searched_books = Book.objects.filter(title__icontains=name_of_book)
print(searched_books)
