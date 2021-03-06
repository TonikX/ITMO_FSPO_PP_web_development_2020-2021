# Generated by Django 3.1.7 on 2021-03-07 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_number', models.CharField(max_length=20)),
                ('Brand', models.CharField(max_length=20)),
                ('Model', models.CharField(max_length=20)),
                ('Colour', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Birthdate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_date', models.DateTimeField()),
                ('End_date', models.DateTimeField(null=True)),
                ('ID_car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.car')),
                ('ID_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.carowner')),
            ],
        ),
        migrations.CreateModel(
            name='DrivingLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_id_card', models.CharField(max_length=10)),
                ('Type', models.CharField(max_length=10)),
                ('ID_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.carowner')),
            ],
        ),
    ]
