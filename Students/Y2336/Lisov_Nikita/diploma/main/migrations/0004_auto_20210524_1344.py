# Generated by Django 3.2.3 on 2021-05-24 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_atricles_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atricles',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='atricles',
            name='type',
            field=models.CharField(choices=[('HIS', 'Историческая'), ('LIT', 'Литературная')], max_length=3, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='atricles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]
