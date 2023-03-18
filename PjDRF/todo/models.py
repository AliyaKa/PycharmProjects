from django.db import models

from users.models import CustomUser


class Projects(models.Model):
    title = models.CharField(max_length=32, unique=True)
    repository = models.URLField(blank=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.title


class ToDo(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, models.PROTECT)
    is_complete = models.BooleanField(default=False)
    proj = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

