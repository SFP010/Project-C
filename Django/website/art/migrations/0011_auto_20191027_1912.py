# Generated by Django 2.2.6 on 2019-10-27 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20191027_1912'),
        ('art', '0010_auto_20191023_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='artwork',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.DeleteModel(
            name='Artwork',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]