# Generated by Django 3.1 on 2019-12-13 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='DateTime'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='status',
            field=models.CharField(choices=[('AR', 'Arrived'), ('IM', 'In the making'), ('SE', 'Sent'), ('NP', 'Not paid')], default='IM', max_length=2),
        ),
    ]
