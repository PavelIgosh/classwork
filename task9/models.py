from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Record(models.Model):
    sport = models.CharField(max_length=15)
    result = models.PositiveIntegerField()
    athlete = models.OneToOneField(Athlete, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.athlete}({self.sport}) - {self.result}'
