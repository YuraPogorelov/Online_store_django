from django.shortcuts import render
from .models import Category, Product, CartItem, Cart

# Create your views here.

def base_view(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart,
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    cart = Cart.objects.first()
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
         'cart': cart,
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories
    }
    return render(request, 'category.html', context)

def cart_view(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, "cart.html", context)
