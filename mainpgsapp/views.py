from django.shortcuts import render


def index(request):
    return render(request, 'mainpgsapp/index.html')


def contacts(request):
    return render(request, 'mainpgsapp/contacts.html')


def products(request):
    return render(request, 'mainpgsapp/products.html')
