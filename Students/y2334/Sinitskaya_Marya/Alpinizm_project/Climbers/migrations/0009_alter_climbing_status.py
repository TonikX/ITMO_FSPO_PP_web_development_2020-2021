# Generated by Django 3.2.4 on 2021-06-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Climbers', '0008_auto_20210614_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbing',
            name='status',
            field=models.CharField(choices=[('Планируется', 'Планируется'), ('Выполняется', 'Выполняется'), ('Завершен', 'Завершен')], default='Планируется', max_length=20, verbose_name='Статус'),
        ),
    ]
