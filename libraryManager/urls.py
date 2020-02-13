from django.urls import path
from . import views

app_name = 'libraryManager'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.detail, name='detail'),
    path('book/<int:book_id>/flag', views.flag, name='readflag')
]
