from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    prod_image = models.FileField(upload_to='shop/', null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=7,default=1999)

    def __str__(self):
        return self.title

