# Generated by Django 3.1.4 on 2020-12-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='donate_to',
            field=models.ManyToManyField(to='hospital.Hospital'),
        ),
    ]
