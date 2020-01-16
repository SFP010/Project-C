# Generated by Django 2.2.6 on 2020-01-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0034_artwork_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='category',
            field=models.CharField(choices=[('photography', 'Photography'), ('fineArt', 'FineArt'), ('graphic', 'Graphic'), ('drawing', 'Drawing')], default='', max_length=60),
        ),
    ]