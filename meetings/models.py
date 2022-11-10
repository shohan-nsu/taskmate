from django.db import models
from datetime import time

class Meeting(models.Model):
    title = models.CharField(max_length= 200)
    date = models.DateField()
    start_time = models.TimeField(default = time(9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

class Room(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title