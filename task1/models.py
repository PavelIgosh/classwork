from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=25, verbose_name="Название")
    publication_date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    genre = models.ManyToManyField('Genre')
    author = models.ManyToManyField('Author')

    def __str__(self):
        return f"{self.title}:{' / '.join([a.name for a in self.author.all()])}"
