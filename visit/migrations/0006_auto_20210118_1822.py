# Generated by Django 3.0.6 on 2021-01-18 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visit', '0005_information_cel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='target',
        ),
        migrations.AlterField(
            model_name='information',
            name='cel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
