# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewProductForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def new_product(request):
    if request.method == "POST":
        form = NewProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_list')
    else:
        form = NewProductForm()
    return render(request, 'new_product.html', {'form': form})
