# Generated by Django 2.0.1 on 2018-03-13 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliked_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.WizzerUser')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.WizzerUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='whiz',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='whiz',
            name='likes',
        ),
        migrations.AddField(
            model_name='like',
            name='whiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Whiz'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='whiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Whiz'),
        ),
    ]