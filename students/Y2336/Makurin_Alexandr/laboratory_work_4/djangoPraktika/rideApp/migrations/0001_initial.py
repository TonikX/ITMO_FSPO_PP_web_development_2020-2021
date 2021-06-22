# Generated by Django 3.2.4 on 2021-06-12 14:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('directorSurname', models.CharField(max_length=50)),
                ('childrenPrice', models.BigIntegerField()),
                ('discountPrice', models.BigIntegerField()),
                ('adultPrice', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('startDate', models.DateField(default=datetime.datetime(2021, 6, 12, 17, 30, 9, 479167))),
                ('lifetime', models.BigIntegerField()),
                ('basePrice', models.BigIntegerField()),
                ('playground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideApp.playground')),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime(2021, 6, 12, 17, 30, 9, 479167))),
                ('childrenSales', models.BigIntegerField()),
                ('discountSales', models.BigIntegerField()),
                ('adultSales', models.BigIntegerField()),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideApp.ride')),
            ],
        ),
    ]
