# Generated by Django 3.0.6 on 2021-02-12 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_wiadomosc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wiadomosc',
            old_name='read',
            new_name='czytano',
        ),
    ]
