import imp
from itertools import product
from pyexpat import model
from re import template
from unittest import loader
from urllib import request
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Customer
from .tables import ProductTable

# URL configurations 

'''
def test(request):
    return render(request, 'store/main.html', {'name': 'Shaka Juma'})
    #return HttpResponse('Hello juma world')
'''

# render all products in a table # http://127.0.0.1:9000/store/table

def viewProducts(request):
    product = Product.objects.all()
    return render(request, 'store/main3.html', {'products': list(product)})

# view a list of products # http://127.0.0.1:9000/store/

def products(request):
    product_list = Product.objects.order_by('last_update')
    template = loader.get_template('store/main2.html')
    context = { 'product_list' : product_list,}
    return render(request, 'store/main2.html', context)


# view a single product # http://127.0.0.1:9000/store/1/

def oneProduct(request, id):
    product = Product.objects.get(pk = id)
    return render(request, 'store/main4.html', {'product': product})

# reduce inventory 

def reduceInventory(request, pk):
    product = Product.objects.get(pk = pk)
    quantity = request.POST
    inventory = inventory - quantity
    inventory.save()
    return render(request, 'store/inventory.html', {'product': product})


