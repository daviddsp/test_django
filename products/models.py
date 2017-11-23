
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    keywords = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('name',)