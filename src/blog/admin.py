from django.contrib import admin

from .models import Categories, Posts


admin.site.register(Categories)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
