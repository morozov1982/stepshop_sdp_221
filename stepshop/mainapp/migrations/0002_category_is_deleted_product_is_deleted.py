# Generated by Django 4.2.5 on 2023-12-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
