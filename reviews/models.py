from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(
        UserProfile, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    product = models.ForeignKey(
        Product, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    review = models.CharField(max_length=254)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2
        )
    # date = models.DateField(default=date.today)

    def __str__(self):
        return self.review
