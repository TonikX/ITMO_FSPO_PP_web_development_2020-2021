# Generated by Django 3.2.3 on 2021-06-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inhabitation',
            name='in_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='inhabitation',
            name='out_date',
            field=models.DateField(),
        ),
    ]
