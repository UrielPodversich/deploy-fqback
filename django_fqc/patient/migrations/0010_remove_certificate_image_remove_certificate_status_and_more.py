# Generated by Django 4.1 on 2022-10-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_patient_city_patient_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='image',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='status',
        ),
        migrations.AddField(
            model_name='certificate',
            name='image_binary',
            field=models.BinaryField(null=True),
        ),
    ]
