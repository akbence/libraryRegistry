from django.shortcuts import render, get_object_or_404
from django.views import generic

from libraryManager.models import Book

class IndexView(generic.ListView):
    template_name = 'libraryManager/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model = Book
    template_name = 'libraryManager/detail.html'
    context_object_name = 'book'

def flag(request, book_id):
    print(book_id)
    detailed_book = get_object_or_404(Book, pk=book_id)
    detailed_book.already_read = not detailed_book.already_read
    detailed_book.save()
    context = {
        'book': detailed_book
    }
    return render(request, 'libraryManager/detail.html', context)


def add(request,book):
    return None