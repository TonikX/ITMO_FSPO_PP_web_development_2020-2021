# Generated by Django 3.1.7 on 2021-03-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_auto_20210327_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='password',
            field=models.CharField(default='a', max_length=16),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='username',
            field=models.CharField(default='a', max_length=16, unique=True),
        ),
    ]
