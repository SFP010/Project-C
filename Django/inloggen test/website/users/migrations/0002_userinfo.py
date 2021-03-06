# Generated by Django 3.1 on 2019-10-26 08:43

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('lname_prefix', models.CharField(max_length=60, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('address_street_name', models.CharField(max_length=60, null=True)),
                ('address_house_nr', models.CharField(max_length=60, null=True)),
                ('address_house_nr_addition', models.CharField(max_length=60, null=True)),
                ('address_postcode', models.CharField(max_length=60, null=True)),
                ('address_city', models.CharField(max_length=60, null=True)),
                ('address_country', models.CharField(max_length=60, null=True)),
                ('language', models.CharField(default='English', max_length=60)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
