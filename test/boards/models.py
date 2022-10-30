from django.db import models
from django.conf import settings


class Board(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    play_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='play_board')
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
