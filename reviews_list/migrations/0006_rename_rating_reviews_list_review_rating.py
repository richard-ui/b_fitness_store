# Generated by Django 3.2 on 2021-08-28 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_list', '0005_alter_reviews_list_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews_list',
            old_name='rating',
            new_name='review_rating',
        ),
    ]
