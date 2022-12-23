# Generated by Django 3.2.16 on 2022-12-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=6000),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
