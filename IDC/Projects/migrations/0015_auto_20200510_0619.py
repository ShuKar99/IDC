# Generated by Django 3.0.5 on 2020-05-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0014_students_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images/Sponsorimages'),
        ),
    ]
