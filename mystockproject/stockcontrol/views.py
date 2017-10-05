# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
