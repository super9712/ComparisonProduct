# aspectapp/models.py

from django.db import models

class Product(models.Model):
    object_name = models.CharField(max_length=200)
    img_text = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return self.object_name