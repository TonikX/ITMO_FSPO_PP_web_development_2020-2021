# Generated by Django 3.2.4 on 2021-06-13 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Climbers', '0004_waypoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbing',
            name='mountain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Climbers.mountain', verbose_name='Вершина'),
        ),
    ]
