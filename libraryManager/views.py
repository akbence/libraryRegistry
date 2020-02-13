from django.shortcuts import render
from django.http import response

from libraryManager.models import Book


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }
    return render(request, 'libraryManager/index.html', context)


def detail(request, book_id):

    detailed_book = Book.objects.get(pk=book_id)
    context = {
        'book': detailed_book
    }
    return render(request, 'libraryManager/detail.html', context)
