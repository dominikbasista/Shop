import pdb
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product, Category
from cart.forms import CartAddProductForm


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category,
               'categories': categories,
               'products': products}

    return render(request, 'shop/product/list.html', context=context)


def product_detail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    category = None
    print(category)
    categories = Category.objects.all()
    category = product.category
    context = {'product': product, 'cart_product_form': cart_product_form, 'categories': categories, 'category':category}
    return render(request, 'shop/product/detail.html', context=context)



