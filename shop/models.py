
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Store(models.Model):

    store_name = models.CharField(max_length=70)
    store_type = models.CharField(max_length=40,  default='General' )
    store_logo = models.CharField(max_length=500, default='null')
    store_link = models.CharField(max_length=120)

    def __str__(self):
        return self.store_name


class Comment(models.Model):

    store = models.ForeignKey(Store, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.store)

