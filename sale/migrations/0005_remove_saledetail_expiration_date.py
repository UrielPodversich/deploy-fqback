# Generated by Django 4.1 on 2022-10-11 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_alter_sale_patient_alter_saledetail_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saledetail',
            name='expiration_date',
        ),
    ]
