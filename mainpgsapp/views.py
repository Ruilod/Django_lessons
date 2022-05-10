import random

from django.shortcuts import render

from mainpgsapp.models import Product, ProductCategory


def index(request):
    products = Product.objects.all()[:4]
    context = {
        'title': 'Стульгазин',
        'products': products
    }
    return render(request, 'mainpgsapp/index.html', context=context)


def contacts(request):
    return render(request, 'mainpgsapp/contacts.html')


def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'title': 'Стульгазин',
        'products': products[:3],
        'hot': random.choice(products),
        'categories': categories
    }
    return render(request, 'mainpgsapp/products.html', context=context)


def product(request, id):
    print(id)