# Generated by Django 2.0.1 on 2018-03-08 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0009_wizzeruser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wizzeruser',
            name='profile_picture',
            field=models.FileField(default='', upload_to='uploads'),
        ),
    ]
