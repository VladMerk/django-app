from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<int:id>', views.detail_category, name='categories'),
    path('categories/', views.detail_category, name='categories_index'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
]
