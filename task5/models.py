from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.CharField(max_length=32)

    library = models.ForeignKey(Library, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}: {self.library}'
