# Generated by Django 3.2.5 on 2021-07-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorialOffice',
            fields=[
                ('id_editorial_office', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=75, verbose_name='Имя редактора')),
            ],
        ),
    ]
