# Generated by Django 3.1.4 on 2020-12-09 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_donor_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddrive',
            name='donate_to',
        ),
    ]
