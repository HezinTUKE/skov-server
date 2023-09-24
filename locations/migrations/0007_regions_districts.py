# Generated by Django 4.0.10 on 2023-09-20 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_remove_regions_coutry_delete_districts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=20)),
                ('coutry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.country')),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=20)),
                ('psc', models.CharField(max_length=15)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.regions')),
            ],
        ),
    ]
