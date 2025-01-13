from django.db import models


class School(models.Model):
    name = models.CharField(max_length=32)
    people_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=32)

    school = models.OneToOneField(School, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.school}"
