# Generated by Django 4.2.7 on 2023-12-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_usermodel_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='date_of_birth',
            field=models.DateField(blank=True, default=''),
        ),
    ]
