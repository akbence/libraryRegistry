from django.contrib import admin

# Register your models here.
from .models import Book,Category

@admin.register(Category,Book)
class LibraryManagerAdmin(admin.ModelAdmin):
    pass

