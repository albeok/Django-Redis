from django.db import models

class Product(models.Model):
    name_product = models.CharField(max_length=20)
    description = models.TextField()
    tex_id = models.CharField(max_length=40)

    def __str__(self):
        return self.name_product
