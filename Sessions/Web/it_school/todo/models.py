from django.db import models

# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    resolved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
