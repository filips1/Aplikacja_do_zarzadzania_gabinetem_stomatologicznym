# Generated by Django 3.0.6 on 2021-01-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tooth', '0003_remove_tooth_destructions_healed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='tooth',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]