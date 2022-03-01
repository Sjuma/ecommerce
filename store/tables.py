from pyexpat import model
from django_tables2 import tables
from .models import Product

class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap.html"
        fields = ('product_name', 'unit_price')