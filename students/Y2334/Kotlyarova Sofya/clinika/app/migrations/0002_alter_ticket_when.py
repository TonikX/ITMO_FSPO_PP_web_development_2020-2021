# Generated by Django 3.2.4 on 2021-07-01 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='when',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
