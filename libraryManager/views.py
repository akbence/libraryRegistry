from django.shortcuts import render
from django.http import response

from libraryManager.models import Book


def index(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        html += '<h2>' + book.author + ' - ' + book.title + '</h2>'
    return response.HttpResponse("<h1>Library<h1>"+html)


def detail(request, book_id):

    return response.HttpResponse(book_id)
