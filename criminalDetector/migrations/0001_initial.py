# Generated by Django 3.1.2 on 2021-05-14 07:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='Criminal_Images')),
                ('crimeDetail', models.CharField(max_length=5000)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('relativeContact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='police',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='pics')),
                ('idCardImg', models.ImageField(upload_to='idCard')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='searches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Searched_Criminals')),
            ],
        ),
    ]
