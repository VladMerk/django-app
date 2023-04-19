from django.db import models

from blog.models import Categories


class Menu(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        ordering = ['title']
