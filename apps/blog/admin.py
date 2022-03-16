from django.contrib import admin
from apps.blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'enabled']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
