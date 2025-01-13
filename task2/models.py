from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=32)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=32)
    date = models.DateField()
    attendee = models.ManyToManyField('Attendee')

    def __str__(self):
        return f'{self.name}: {" / ".join([a.name for a in self.attendee.all()])}'
