# Generated by Django 3.2.4 on 2021-06-12 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Climbers', '0003_auto_20210612_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('waypoint_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('waypoint_name', models.CharField(max_length=75, verbose_name='Название вершины')),
                ('waypoint_desc', models.CharField(max_length=200, verbose_name='Описание')),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Climbers.mountain', verbose_name='Гора')),
            ],
        ),
    ]
