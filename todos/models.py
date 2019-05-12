from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.TextField()
    deadline = models.TextField()
    progress = models.CharField(max_length=4)
    objects = models.Manager()

    def __str__(self):
        return self.name

