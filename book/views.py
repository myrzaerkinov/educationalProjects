from django.http import HttpResponse
from django.shortcuts import render
from . import models

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})