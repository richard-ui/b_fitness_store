from django.db import models
from products.models import Product
from profiles.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Reviews_list(models.Model):
    user = models.ForeignKey(
        UserProfile, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    product = models.ForeignKey(
        Product, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    review = models.CharField(max_length=254)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
