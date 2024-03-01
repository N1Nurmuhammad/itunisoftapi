# Generated by Django 5.0.1 on 2024-01-19 11:46

import django.utils.timezone
import main.models.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
                ('google_maps', models.URLField(blank=True, null=True)),
                ('yandex_maps', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to=main.models.main.doc_upload_location)),
                ('size', models.CharField(blank=True, help_text='automatic generated', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurPartnersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to=main.models.main.partners_upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='OurStatisticsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('customer_status', models.IntegerField(default=100)),
                ('projects_count', models.IntegerField()),
                ('employees_count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='technologiesmodel',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]