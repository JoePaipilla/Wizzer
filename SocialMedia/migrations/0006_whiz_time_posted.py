# Generated by Django 2.0.1 on 2018-03-03 04:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0005_whiz_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiz',
            name='time_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
