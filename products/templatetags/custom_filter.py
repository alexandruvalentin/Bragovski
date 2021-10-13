from django import template
from products.models import Product
import random

register = template.Library()


@register.filter(name='filter_shuffle')
def filter_shuffle(products):
    products = Product.objects.all()
    shuffled_products = [product for product in products]
    random.shuffle(shuffled_products)
    return shuffled_products
