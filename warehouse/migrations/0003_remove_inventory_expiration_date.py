# Generated by Django 4.1 on 2022-10-11 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_alter_inventory_warehouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='expiration_date',
        ),
    ]
