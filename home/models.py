from django.db import models

# Create your models here.


class Product_item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=124)
    qty = models.IntegerField()

    def __str__(self):
        return self.title
