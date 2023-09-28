from django.db import models

# Create your models here.
class Inventory():
    name = models.Charfield(max_length=255)