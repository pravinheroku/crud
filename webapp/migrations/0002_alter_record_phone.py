# Generated by Django 3.2.23 on 2024-01-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
