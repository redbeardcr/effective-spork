# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    SKU = models.CharField(max_length=10, unique='true')

    def __str__(self):
        return self.name
