from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models

def book_all(request):
    genre = models.Genre.objects.all()
    return render(request, 'book_list.html', {'genre': genre})

def book_detail(request, id):
    book = get_object_or_404(models.Genre, id=id)
    return render(request, 'book_detail.html', {'book': book})


