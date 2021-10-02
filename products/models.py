from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    available = models.BooleanField(default=False)