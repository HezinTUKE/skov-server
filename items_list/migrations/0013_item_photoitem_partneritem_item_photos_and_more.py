# Generated by Django 4.0.10 on 2023-09-23 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_usermodel_date_of_birth'),
        ('items_list', '0012_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('active_time', models.DateTimeField()),
                ('title', models.CharField(max_length=15)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_list.categorylang')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='./imgs/items')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('item', models.ManyToManyField(to='items_list.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='photos',
            field=models.ManyToManyField(to='items_list.photoitem'),
        ),
        migrations.AddField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_list.subcategory'),
        ),
    ]
