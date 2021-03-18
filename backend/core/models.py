from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """Base post model."""
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)  # height_field=None, width_field=None, max_length=100
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # published_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        author =(
            f"{self.author.first_name} {self.author.last_name}"
            if self.author.first_name and self.author.last_name
            else self.author
        )
        return self.title


class Comment(models.Model):
    """Base comment model."""

    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=255)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text
