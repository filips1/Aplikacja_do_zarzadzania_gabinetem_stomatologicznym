# Generated by Django 3.0.6 on 2020-12-08 17:58

import account.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Login')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='data dołączenia')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='data ostatniego zalogowania')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_dentist', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(default='default_profile.jpg', upload_to='profile_pic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20, verbose_name='Imię')),
                ('Surname', models.CharField(max_length=30, verbose_name='nazwisko')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Numer telefonu musi zawierać od 9-15 znaków i pierwszym znakiem może być +', regex='^\\+?1?\\d{9,15}$')])),
                ('city', models.CharField(max_length=30, verbose_name='Miejscowość')),
                ('clinic_adress', models.CharField(max_length=50, verbose_name='Adres Kliniki')),
                ('about_me', models.TextField(blank=True, max_length=1000)),
                ('account', models.OneToOneField(limit_choices_to={'is_dentist': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specialisation', models.CharField(max_length=50)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dentist')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20, verbose_name='Imię')),
                ('Surname', models.CharField(max_length=30, verbose_name='nazwisko')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Numer telefonu musi zawierać od 9-15 znaków i pierwszym znakiem może być +', regex='^\\+?1?\\d{9,15}$')])),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Miejscowość')),
                ('adress', models.CharField(blank=True, max_length=50, verbose_name='Adres zamieszkania')),
                ('email_conversation', models.EmailField(blank=True, max_length=30, verbose_name='Skrzynka na emaile od dentysty')),
                ('age', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='wiek')),
                ('account', models.OneToOneField(blank=True, limit_choices_to={'is_dentist': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('dentist', models.ManyToManyField(to='account.Dentist')),
            ],
        ),
        migrations.CreateModel(
            name='OtherSites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.URLField()),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dentist')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
                ('dentist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Dentist')),
            ],
        ),
        migrations.CreateModel(
            name='Images_aboutme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to=account.models.get_user_image_folder)),
                ('about', models.CharField(max_length=30, verbose_name='opis')),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dentist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='opis')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='stworzone')),
                ('active', models.BooleanField(default=True, verbose_name='aktywne')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dentist')),
            ],
            options={
                'verbose_name': 'Komentarz',
                'verbose_name_plural': 'Komentarze',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=50)),
                ('significance', models.TextField(choices=[('1', 'Duża'), ('2', 'Średnia'), ('3', 'Mała')])),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dentist')),
            ],
        ),
    ]
