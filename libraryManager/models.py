from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    already_read = models.BooleanField(default=False)
    date_of_read = models.DateField(default=None, null=True, blank=True)
    date_of_create = models.DateField(default=None)

    def get_absolute_url(self):
        return reverse('libraryManager:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.author) + ' - ' + str(self.title)
