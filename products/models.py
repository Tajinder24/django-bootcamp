from django.db import models

# Create your models here.
class Product(models.Model):
    #id = models.AutoField()
    title = models.CharField(max_length = 220)
    content = models.TextField(blank = True, null = True)
    price = models.IntegerField(default = 0)