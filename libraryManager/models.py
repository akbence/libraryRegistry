from django.db import models


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
    date_of_read = models.DateField()
    def __str__(self):
        return str(self.author) + ' - ' + str(self.title)
