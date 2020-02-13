from django.shortcuts import render, get_object_or_404

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


def flag(request, book_id):
    print(book_id)
    detailed_book = get_object_or_404(Book, pk=book_id)
    detailed_book.already_read = not detailed_book.already_read
    detailed_book.save()
    context = {
        'book': detailed_book
    }
    return render(request, 'libraryManager/detail.html', context)
