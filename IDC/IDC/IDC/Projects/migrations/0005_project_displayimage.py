# Generated by Django 3.0.5 on 2020-05-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_merge_20200502_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='displayImage',
            field=models.ImageField(default='static/images/deafaultProject.png', upload_to=''),
        ),
    ]