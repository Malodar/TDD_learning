from django.db import models

# Create your models here.


class Item(models.Model):
    """List element"""
    text = models.TextField(default='')
