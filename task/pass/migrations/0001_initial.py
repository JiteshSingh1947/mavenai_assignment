# Generated by Django 2.1 on 2020-07-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('passportno', models.CharField(max_length=20)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('phoneNumber', models.CharField(default=None, max_length=12)),
                ('img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
