# Generated by Django 3.2 on 2021-06-22 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_list', '0003_alter_reviews_list_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews_list',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
