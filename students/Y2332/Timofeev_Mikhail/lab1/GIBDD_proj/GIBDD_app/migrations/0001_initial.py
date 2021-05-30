# Generated by Django 3.1.7 on 2021-05-30 15:55

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.TextField()),
                ('body_model', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=10, unique=True)),
                ('helm', models.BooleanField()),
                ('drive', models.BooleanField()),
                ('year', models.IntegerField()),
                ('owner_type', models.BooleanField()),
                ('district', models.TextField()),
                ('year_tax', models.FloatField()),
                ('comment', models.TextField()),
                ('color', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.TextField(unique=True)),
                ('power', models.IntegerField()),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inspector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_number', models.CharField(max_length=7, unique=True)),
                ('fullname', models.TextField()),
                ('post', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LegalOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_inn', models.CharField(max_length=10, unique=True)),
                ('owner_name', models.CharField(max_length=60)),
                ('chief', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField(unique=True)),
                ('owner_fullname', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.CharField(max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WatchInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_date', models.DateField()),
                ('sign_cost', models.FloatField()),
                ('watch_cost', models.FloatField()),
                ('mileage', models.FloatField()),
                ('okay', models.BooleanField()),
                ('reasons', models.TextField(null=True)),
                ('car_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.car')),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.inspector')),
            ],
        ),
        migrations.CreateModel(
            name='DriveAwayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driving_away', models.BooleanField()),
                ('date_away', models.DateField(null=True)),
                ('date_return', models.DateField(null=True)),
                ('car_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(unique=True)),
                ('brand', models.CharField(max_length=15)),
                ('producer', models.CharField(max_length=60)),
                ('body_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.body')),
                ('engine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.engine')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.carmodel'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.physicalowner'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner_inn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GIBDD_app.legalowner'),
        ),
    ]
