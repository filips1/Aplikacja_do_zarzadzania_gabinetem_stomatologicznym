# Generated by Django 3.0.6 on 2021-02-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20210212_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wiadomosc',
            old_name='nowy_cel',
            new_name='target',
        ),
        migrations.DeleteModel(
            name='Informations',
        ),
    ]
