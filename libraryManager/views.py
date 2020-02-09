from django.shortcuts import render
from django.http import response

# Create your views here.

def index(request):
    return response.HttpResponse("<h1>This is sample library homepage<h1>")
