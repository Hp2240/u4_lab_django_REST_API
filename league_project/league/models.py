from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    record = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
