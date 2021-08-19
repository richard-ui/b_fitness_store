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
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=254,  null=True, blank=True)

    def __str__(self):
        return str(self.name)
