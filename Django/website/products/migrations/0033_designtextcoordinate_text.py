# Generated by Django 3.0 on 2019-12-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20191219_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='designtextcoordinate',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
