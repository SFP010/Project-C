# Generated by Django 3.0 on 2019-12-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_design_design_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_photo',
            field=models.ImageField(blank=True, null=True, upload_to='design_pics'),
        ),
    ]