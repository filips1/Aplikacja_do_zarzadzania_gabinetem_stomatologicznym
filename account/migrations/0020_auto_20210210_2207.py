# Generated by Django 3.0.6 on 2021-02-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='dentist',
            field=models.ManyToManyField(blank=True, null=True, to='account.Dentist'),
        ),
        migrations.AlterField(
            model_name='location',
            name='receptionist',
            field=models.ManyToManyField(blank=True, null=True, to='account.Receptionist'),
        ),
    ]
