#from unicodedata import name
from ast import Or 
from django.db import models
from django.contrib.auth.models import User

#create your models here
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank= True)
        
    #   return a string of category name 
    def __str__(self) -> str:
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    inventory = models.IntegerField(null=True)
    last_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    product_image = models.ImageField(null=True, blank=True)

     #   return a string of product name 
    def __str__(self) -> str:
        return self.product_name



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

     #   return a string of customer name
    def __str__(self) -> str:
        return f'({self.last_name} {self.first_name})'

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

     #   return a string of order id 
    def __str__(self) -> str:
        return self.id


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

     #   return a string of order item ID
    def __str__(self) -> str:
        return self.id


class CustomerAddress(models.Model):
    estate = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

     #   return a string of customer address
    def __str__(self) -> str:
        return f'{self.estate} {self.street}'


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

     #   return a string of Cart id
    def __str__(self) -> str:
        return self.id


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    #   return a string of Cart item id
    def __str__(self) -> str:
        return self.id
