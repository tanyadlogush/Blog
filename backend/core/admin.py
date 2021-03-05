from django.contrib import admin

# Register your models here.

from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_filter = ('author', 'post')
    list_display = ('__str__', 'author', 'post')


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('author',)
    inLines = (CommentInLine,)
