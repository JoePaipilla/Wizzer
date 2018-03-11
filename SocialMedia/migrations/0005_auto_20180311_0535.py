# Generated by Django 2.0.1 on 2018-03-11 09:35

import SocialMedia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0004_auto_20180311_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wizzeruser',
            name='background_image',
            field=models.FileField(default='settings.MEDIA_ROOT/default/default-background.jpg', upload_to=SocialMedia.models.background_image_path),
        ),
        migrations.AlterField(
            model_name='wizzeruser',
            name='profile_picture',
            field=models.FileField(default='settings.MEDIA_ROOT/default/default-background.jpg', upload_to=SocialMedia.models.profile_picture_path),
        ),
    ]
