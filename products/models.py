from django.db import models
from django.db.models import Avg

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        'Category', null=True,
        blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_shoe_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(
        null=True, blank=True
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name