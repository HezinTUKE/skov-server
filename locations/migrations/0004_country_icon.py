# Generated by Django 5.0.1 on 2024-02-26 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0003_initial'),
        ('locations', '0003_remove_country_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='icons.icon'),
        ),
    ]