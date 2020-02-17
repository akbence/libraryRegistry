from django.db import models
from django.urls import reverse
from django.utils import timezone

from libraryManager.soft_delete_query_set import SoftDeletableManager


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    objects = SoftDeletableManager()
    archive_objects = models.Manager()
    deleted_ts = models.DateTimeField(null=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    already_read = models.BooleanField(default=False)
    date_of_read = models.DateField(default=None, null=True, blank=True)
    date_of_create = models.DateField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('libraryManager:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.author) + ' - ' + str(self.title)

    def delete(self):
        """Softly delete the entry"""
        self.deleted_ts = timezone.now()
        self.save()

    def hard_delete(self):
        """Remove the entry from the database permanently"""
        super().delete()
