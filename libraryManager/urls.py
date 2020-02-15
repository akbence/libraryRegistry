from django.urls import path
from . import views

app_name = 'libraryManager'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<pk>', views.DetailView.as_view(), name='detail'),
    path('book/<int:book_id>/flag', views.flag, name='readflag'),
    path('add', views.BookCreate.as_view(), name='add-form'),
    path('update/<pk>', views.BookUpdate.as_view(), name='update-form'),
    path('delete/<pk>', views.BookDelete.as_view(), name='delete'),
]
