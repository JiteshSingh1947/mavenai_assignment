# Generated by Django 2.1 on 2020-07-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0007_auto_20200725_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='box.jpg', upload_to='media/'),
        ),
    ]
