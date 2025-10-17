from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name