# Generated by Django 3.2.3 on 2021-05-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_writer_bibliografi'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='about_life',
            field=models.TextField(default=2, verbose_name='Произведения о жизни'),
            preserve_default=False,
        ),
    ]
