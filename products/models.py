from django.db import models

# Create your models here.
"""class Product:
         id : Primary key
         name : str
         category : str
         decsription : str
         image_url : str
         rating : floating 2 decimal_places 

"""
class Product(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    image_url = models.ImageField(upload_to='product_imgs/',default='default.png')
    rating = models.FloatField()


def __str__(self):
    return f"< Product {self.name} >"
