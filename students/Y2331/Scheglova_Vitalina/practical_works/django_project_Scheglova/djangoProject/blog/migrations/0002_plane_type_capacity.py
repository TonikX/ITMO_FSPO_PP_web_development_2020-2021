# Generated by Django 3.2 on 2021-05-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane_type',
            name='capacity',
            field=models.IntegerField(default=150),
            preserve_default=False,
        ),
    ]
