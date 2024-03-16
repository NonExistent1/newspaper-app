from django.contrib import admin

from .models import Article, Comment

class CommentInline(admin.TabularInline):
    """Inline for seeing comments related to the article"""
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    """Custom Article Admin"""
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)