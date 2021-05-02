from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=124)
    qty = models.IntegerField()

    def __str__(self):
        return self.name