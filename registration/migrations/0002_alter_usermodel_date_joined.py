# Generated by Django 4.2.7 on 2023-12-03 21:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
