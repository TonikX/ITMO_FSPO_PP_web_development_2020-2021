# Generated by Django 3.2.4 on 2021-06-21 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0003_auto_20210619_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='comment',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='solution',
            name='jury',
            field=models.ForeignKey(blank=True, default='None', on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solution',
            name='score',
            field=models.FloatField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to=settings.AUTH_USER_MODEL),
        ),
    ]