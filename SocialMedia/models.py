from django.db import models


class WizzerUser(models.Model):
    first_name = models.CharField(max_length=30, default="")
    second_name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.username


class Whiz(models.Model):
    whiz_poster = models.ForeignKey(WizzerUser, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return "[{}] WHIZ #{} - {}".format(self.whiz_poster, self.id, self.content)