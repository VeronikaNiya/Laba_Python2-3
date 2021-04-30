from django.contrib import admin

from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    category = ('title', 'text')
    slug = ('slug', 'text',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    title = ('title', 'text',)
    slug = ('slug', 'text',)
    # pub_date = ('title', 'published',)
