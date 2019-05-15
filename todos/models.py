from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    name = models.TextField(max_length=160)
    deadline = models.TextField(max_length=160)
    progress = models.CharField(max_length=4)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todos-viewtodo', kwargs={'pk': self.pk})    

