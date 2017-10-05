# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_list_or_404
from .forms import NewProductForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


#def new_product(request):
#    return render(request, 'new_product.html')


def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect('product_list')  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_product.html', {'form': form})