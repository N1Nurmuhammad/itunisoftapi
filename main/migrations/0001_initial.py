# Generated by Django 5.0.1 on 2024-01-19 04:23

import main.models.main
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=main.models.main.upload_location)),
                ('title', models.CharField(max_length=255)),
                ('header', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('play_market', models.URLField(blank=True, null=True)),
                ('app_store', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=main.models.main.upload_location)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TechnologiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=main.models.main.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to=main.models.main.upload_location)),
                ('text', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('items', models.ManyToManyField(to='main.serviceitemsmodel')),
                ('backend', models.ManyToManyField(related_name='bservices', to='main.technologiesmodel')),
                ('frontend', models.ManyToManyField(related_name='fservices', to='main.technologiesmodel')),
            ],
        ),
    ]
