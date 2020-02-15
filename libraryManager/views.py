from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
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


class BookCreate(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'category', 'page', 'already_read', 'date_of_read']


class BookUpdate(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'category', 'page', 'already_read', 'date_of_read']


class BookDelete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('libraryManager:index')
