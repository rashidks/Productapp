from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class Customer(AbstractUser):
    pass
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__self(self):
        return self.name
    
class Product(models.Model):
    image=models.ImageField(upload_to='product_images/',null=True,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField( max_digits=10, decimal_places=2)
    categories=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__self(self):
        return self.title