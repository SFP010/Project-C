# Generated by Django 2.2.6 on 2019-12-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20191108_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(choices=[('', 'Country'), ('netherland', 'Netherland'), ('usa', 'USA'), ('syria', 'Syria'), ('germany', 'Germany'), ('uk', 'United Kingdom')], default='null', max_length=60),
        ),
    ]
