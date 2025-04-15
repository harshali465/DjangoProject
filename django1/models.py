from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    Name = models.CharField(max_length=200)
    Post = models.CharField(max_length=300)
    Contact = models.CharField(max_length=10)
    Email = models.EmailField(max_length=232)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
        return self.title
# Create your models here.
