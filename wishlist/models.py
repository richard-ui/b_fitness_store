from django.db import models
from products.models import Product
from profiles.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Wishlist(models.Model):

    user = models.ForeignKey(
        UserProfile, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    product = models.ForeignKey(
        Product, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name