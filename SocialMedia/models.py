from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django import forms


"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        WizzerUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()"""

def profile_picture_path(instance, filename):
    return '{}/profile-picture/{}'.format(instance.user.username, filename)


def background_image_path(instance, filename):
    return '{}/background-image/{}'.format(instance.user.username, filename)


class WizzerUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    following = models.ManyToManyField('self', blank=True, related_name='following_set', symmetrical=False)
    followers = models.ManyToManyField('self', blank=True, related_name='follower_set', symmetrical=False)
    profile_picture = models.FileField(
        default=r'default\default-profile-picture.jpg', upload_to=profile_picture_path, max_length=100)
    background_image = models.FileField(
        default=r'default\default-background.jpg', upload_to=background_image_path, max_length=100)
    gender = models.CharField(default='', choices=GENDER_CHOICES, max_length=2)

    def __str__(self):
        return self.user.username


class Whiz(models.Model):
    whiz_poster = models.ForeignKey(WizzerUser, on_delete=models.CASCADE)
    content = models.TextField()
    time_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(WizzerUser, blank=True, related_name='like_set')
    dislikes = models.ManyToManyField(WizzerUser, blank=True, related_name='dislike_set')

    def __str__(self):
        return "[{}] {}".format(self.whiz_poster, self.content)
