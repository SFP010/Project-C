# Generated by Django 2.2.6 on 2019-10-27 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191023_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='artwork',
        ),
        migrations.RemoveField(
            model_name='wish',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wish',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Wish',
        ),
    ]
