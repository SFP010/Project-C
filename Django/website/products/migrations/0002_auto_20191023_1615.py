# Generated by Django 3.1 on 2019-10-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191023_1552'),
        ('art', '0009_auto_20191023_1615'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='artwork_id',
            field=models.ForeignKey(on_delete=models.SET('deleted'), to='art.Artwork'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(on_delete=models.SET('deleted'), to='products.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET('unknown'), to='users.User'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='artwork_id',
            field=models.ForeignKey(on_delete=models.SET('deleted'), to='art.Artwork'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product_id',
            field=models.ForeignKey(on_delete=models.SET('deleted'), to='products.Product'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET('unknown'), to='users.User'),
        ),
    ]