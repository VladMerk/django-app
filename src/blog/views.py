from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Categories, Posts


def index(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/index.html', context=context)

def detail_category(request, id=None):
    if id is None:
        return redirect('blog:index')

    category = get_object_or_404(Categories, id=id)
    subcategories = category.child_category.all()
    context = {
        'category': category,
        'subcategories': subcategories
    }
    return render(request, 'blog/category_detail.html', context)

def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
