from django.conf import settings
from django.db import models
from shop.models import products
from django.contrib.auth.models import User

# Create your models here.

class cartlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('cart_id',)
        verbose_name = 'carlist'
        verbose_name_plural = 'cartlists'

    def __str__(self):
        return self.cart_id
        

class items(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('product',)
        verbose_name = 'item'
        verbose_name_plural = 'items'
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def total(self):
        return self.product.price * self.quantity

