# Generated by Django 2.2.6 on 2019-11-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191030_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_photo',
            field=models.ImageField(default='default_product.jpg', upload_to='product_pics'),
        ),
    ]