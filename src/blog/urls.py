from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='categories'),
    path('categories/', views.IndexView.as_view(), name='categories_index'),
    path('post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post'),
]
