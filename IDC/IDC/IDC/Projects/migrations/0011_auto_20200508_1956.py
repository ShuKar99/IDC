# Generated by Django 3.0.5 on 2020-05-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        ('Projects', '0010_merge_20200508_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculties',
            name='profilePic',
        ),
        migrations.RemoveField(
            model_name='students',
            name='profilePic',
        ),
        migrations.AddField(
            model_name='project',
            name='upcoming_events',
            field=models.ManyToManyField(blank=True, related_name='Project', to='Home.Events'),
        ),
    ]