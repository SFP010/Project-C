# Generated by Django 2.2.6 on 2020-01-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0037_merge_20200116_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='category',
            field=models.CharField(choices=[('', 'Choose category'), ('photography', 'Photography'), ('fineArt', 'Fine Art'), ('graphic', 'Graphic'), ('drawing', 'Drawing'), ('modernArt', 'Modern Art')], default='', max_length=60),
        ),
    ]
