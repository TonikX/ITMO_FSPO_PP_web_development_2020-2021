# Generated by Django 3.1.6 on 2021-04-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20210410_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='BirthDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
