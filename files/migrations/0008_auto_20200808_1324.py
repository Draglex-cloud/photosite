# Generated by Django 3.0.7 on 2020-08-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20200808_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]