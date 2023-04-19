from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="child_category",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Posts(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]
