from django.db import models
from products.models import Product
from profiles.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Reviews_list(models.Model):
    # choices for rating dropdown box
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(
        UserProfile, null=True,
        blank=True, on_delete=models.SET_NULL
        )
    product = models.ForeignKey(
        Product, null=True,
        blank=True, on_delete=models.SET_NULL,
        related_name='reviews'
        )
    review = models.CharField(max_length=254)
    # credits: min and max validators (stack overflow)
    review_rating = models.IntegerField( 
        choices=RATING_CHOICES, default=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    
