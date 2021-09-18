# Generated by Django 3.2 on 2021-08-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_shoe_sizes'),
        ('wishlist', '0004_auto_20210817_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]