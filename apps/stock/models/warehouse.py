from django.db import models

class Warehouse(models.Model):
    """
    Warehouse:
        name - Char
        location - Char
        capacity - Int
"""
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

