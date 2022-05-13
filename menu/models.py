from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=10,decimal_places=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
          total += (cart_item.price * cart_item.quantity)
          return int(total)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, 
     related_name='cartitems')
     product = models.ForeignKey(Food, on_delete=models.CASCADE)
     price = models.PositiveIntegerField() 
     quantity = models.PositiveSmallIntegerField()

     @property 
     def total_price(self):
          return int(self.price * self.quantity)  

     def __str__(self):
          return self.product.title