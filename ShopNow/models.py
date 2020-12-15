from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=150,null=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/')
    isAvailable = models.BooleanField()
    seller = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    averageRating = models.FloatField(default=1.0)
    # averageRating = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.productName

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="reviewsRelatedName")
    reviewBy = models.ForeignKey(User, on_delete=models.CASCADE)
    
    review = models.CharField(max_length=200)

class Rating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='ratingRalatedName')
    rating = models.IntegerField(
        default=1,
        validators = [MaxValueValidator(5),MinValueValidator(1)]
    )


class MyCart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
   
    productName = models.ManyToManyField(Product,related_name= 'productnames')
    



class MyOrdersNew(models.Model):
    orderByUser = models.ForeignKey(User , on_delete=models.CASCADE)
    productOrder = models.ForeignKey(Product , on_delete=models.CASCADE)
    