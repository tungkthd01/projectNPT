# Generated by Django 3.2.9 on 2021-12-01 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211130_1714'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blog',
            table='blog',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
