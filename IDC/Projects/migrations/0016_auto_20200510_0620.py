# Generated by Django 3.0.5 on 2020-05-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0015_auto_20200510_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
