# Generated by Django 3.0.6 on 2021-01-18 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210118_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations',
            name='target',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
