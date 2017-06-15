# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Store
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import CommentForm


def home(request):
    return render(request, 'shop/index.html')


def store_list(request):
    stores_list = Store.objects.all()
    paginator = Paginator(stores_list, 4)
    page = request.GET.get('page')
    try:
        stores = paginator.page(page)
    except PageNotAnInteger:
        stores = paginator.page(1)
    except EmptyPage:
        stores = paginator.page(paginator.num_pages)
    return render(request, 'shop/store_list.html', {'page': page, 'stores': stores})


def store_search(request):

    stores = Store.objects.all()
    query = request.GET.get("q")
    if query:
        stores = stores.filter(Q(store_name__icontains=query)|
                 Q(store_type__icontains=query)).distinct()

    return render(request, 'shop/store_search.html', {'stores': stores},{'query': query})






def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    comments = store.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.store = store
            new_comment.save()
            return redirect('comments', store_id=store.id)

    else:
        comment_form = CommentForm()
        return render(request, 'shop/detail.html', {'store': store, 'comments': comments, 'comment_form': comment_form})



