# Generated by Django 3.1.7 on 2021-03-09 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_exhibition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reg', models.DateField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.dog')),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.exhibition')),
            ],
        ),
        migrations.AddField(
            model_name='exhibition',
            name='member',
            field=models.ManyToManyField(through='blog.Participate', to='blog.Dog'),
        ),
    ]