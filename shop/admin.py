# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Store, Comment

# Register your models here.
admin.site.register(Store)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'store', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
