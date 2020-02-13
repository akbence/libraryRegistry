from django.shortcuts import render
from django.http import response
from django.template import loader

from libraryManager.models import Book


def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('libraryManager/index.html')
    context = {
        'all_books': all_books
    }
    return response.HttpResponse(template.render(context,request))


def detail(request, book_id):

    return response.HttpResponse(book_id)
