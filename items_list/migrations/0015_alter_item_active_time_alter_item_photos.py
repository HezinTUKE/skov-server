# Generated by Django 4.0.10 on 2023-09-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_list', '0014_item_country_item_district_item_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='active_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='photos',
            field=models.ManyToManyField(null=True, to='items_list.photoitem'),
        ),
    ]
