# Generated by Django 2.2.6 on 2019-11-17 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0020_auto_20191117_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='upload_date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 21, 27, 42, 317007)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='upload_date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 21, 27, 42, 318006)),
        ),
    ]
