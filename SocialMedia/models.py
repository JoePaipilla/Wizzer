from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver


def user_directory_path(instance, filename):
    return '{}/{}'.format(instance.username, filename)

"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        WizzerUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()"""

class WizzerUser(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    #SUBJECT TO BE DELETED
    first_name = models.CharField(max_length=30, default="")
    second_name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=15, default="")
    #----------------------
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    profile_picture = models.FileField(default='', upload_to=user_directory_path, max_length=100)

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