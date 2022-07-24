# Generated by Django 3.0.6 on 2021-02-10 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_cennik'),
    ]

    operations = [
        migrations.AddField(
            model_name='cennik',
            name='dentist',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.Dentist'),
            preserve_default=False,
        ),
    ]
