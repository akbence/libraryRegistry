from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import View

from libraryManager.forms import RegisterForm, LoginForm, QueryForm
from libraryManager.models import Book


class IndexView(generic.ListView):
    template_name = 'libraryManager/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


class QueryView(View):
    template_name = 'libraryManager/sorted_filtered_list.html'
    #    context_object_name = 'books'
    form_class = QueryForm

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        print(form.fields)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            order_by_title = '' if form.data.get('order') == 'asc' else '-'
            order_by_title += 'title'
            title = form.data.get('title')
            category = form.data.get('category')
            author = form.data.get('author')
            if form.data.get('only_read'):
                books = Book.objects.filter(title__contains=title, author__contains=author, already_read=True).order_by(
                    order_by_title)
            else:
                books = Book.objects.filter(title__contains=title, author__contains=author).order_by(order_by_title)
            print(books)
            return render(request, self.template_name, {'form': form, 'books': books})
        return render(request, self.template_name, {'form': form})


class DetailView(generic.DetailView):
    model = Book
    template_name = 'libraryManager/detail.html'
    context_object_name = 'book'


class BookCreate(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'category', 'page', 'already_read', 'date_of_read']


class BookUpdate(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'category', 'page', 'already_read', 'date_of_read']


class BookDelete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('libraryManager:index')


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'libraryManager/account_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'register': True})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('libraryManager:index')
        return render(request, self.template_name, {'form': form})


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'libraryManager/account_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'login': True})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        print("here we are")

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    return redirect('libraryManager:index')
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('libraryManager:index')
