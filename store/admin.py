from itertools import product
from statistics import mode
from django.contrib import admin
from . import models

# Register your models here.
# customized listing during registation of objects
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'inventory', 'unit_price']
    list_per_page = 5
    list_editable = ['inventory', 'unit_price']
admin.site.register(models.Product, ProductAdmin)

@admin.register(models.Customer)
class CUstomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    list_editable = ['phone']
    list_per_page = 5

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'payment_status']
    list_per_page = 5

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'unit_price']
    list_per_page = 5

@admin.register(models.CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'city', 'estate', 'street']
    list_per_page = 5

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['created_at']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    list_per_page = 5

admin.site.register(models.CartItem, CartItemAdmin)
