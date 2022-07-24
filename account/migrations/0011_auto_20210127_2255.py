# Generated by Django 3.0.6 on 2021-01-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_invitation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receptionist',
            name='dentist',
        ),
        migrations.AddField(
            model_name='dentist',
            name='receptionist',
            field=models.ManyToManyField(to='account.Receptionist'),
        ),
    ]
