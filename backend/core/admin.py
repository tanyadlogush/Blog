from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_filter = ('author', 'post', 'published_date')
    list_display = ('__str__', 'author', 'post', 'published_date')


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body', )
    list_filter = ('author', 'updated_at')
    list_display = ('__str__', 'author', 'updated_at', 'image')
    inlines = (CommentInLine,)
