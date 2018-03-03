from django.db import models
from django.utils import timezone

class WizzerUser(models.Model):
    first_name = models.CharField(max_length=30, default="")
    second_name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=15, default="")
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Whiz(models.Model):
    whiz_poster = models.ForeignKey(WizzerUser, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "[{}] WHIZ #{} - {}".format(self.whiz_poster, self.id, self.content)