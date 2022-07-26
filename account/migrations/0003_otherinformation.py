# Generated by Django 3.0.6 on 2021-01-18 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210103_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_change', models.DateTimeField()),
                ('type_of', models.TextField(choices=[('zatwierdzenie', 'Zatwierdzone'), ('odwołanie', 'Odwołanie'), ('zmiana daty', 'Zmieniona'), ('usunięta', 'Usunięta'), ('przypomnienie', 'Przypomnienie'), ('czat', 'Czat'), ('zaproszenie', 'Zaproszenie'), ('ogólne', 'Ogólne')])),
                ('read', models.BooleanField(default=False)),
                ('desc', models.TextField()),
                ('target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
