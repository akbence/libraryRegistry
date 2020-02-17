from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'libraryManager'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('query', views.QueryView.as_view(), name='query'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('book/<pk>', login_required(views.DetailView.as_view()), name='detail'),
    path('add', views.BookCreate.as_view(), name='add-form'),
    path('update/<pk>', views.BookUpdate.as_view(), name='update-form'),
    path('delete/<pk>', views.BookDelete.as_view(), name='delete'),
]
