# Generated by Django 3.1.7 on 2021-06-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logach_1', '0003_auto_20210605_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, upload_to='logach\\logach_screens'),
        ),
    ]
