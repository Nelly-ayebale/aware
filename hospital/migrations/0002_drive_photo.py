# Generated by Django 3.1.4 on 2020-12-09 16:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]