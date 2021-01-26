from django.db import models

# Create your models here.
class Ecom(models.Model):
    image=models.ImageField(upload_to='media')
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.title
