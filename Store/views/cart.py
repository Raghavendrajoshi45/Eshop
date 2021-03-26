from django.shortcuts import render, redirect
from Store.models.product import Product
from Store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View



class Cart(View):
    return_url = None
    def get(self , request):
        ids=(list(request.session.get('cart').keys()))
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html',{'products':products})

   