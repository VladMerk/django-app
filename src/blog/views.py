from django.views.generic import DetailView, ListView

from .models import Categories, Posts


class IndexView(ListView):
    queryset = Categories.objects.filter(parent__isnull=True)
    template_name = 'blog/index.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategories'] = context['category'].child_category.all()
        return context


class PostDetailView(DetailView):
    model = Posts
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
