from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post, Comment

# posts = [
#     {'title': 'How to learn VIM', 'author': 'W. Vincent', 'data': '12315'},
#     {'title': 'How to learn Python', 'author': 'Guido van Rossum', 'data': '123145'},
#     {'title': 'How to learn Rust', 'author': 'Fedor', 'data': '1234515'},
# ]

class HomeView(ListView):
    """Base home view."""
    template_name = 'core/home.html'
    queryset = Post.objects.values('title', 'body')


class AboutView(TemplateView):
    """Base about view."""
    template_name = 'core/about.html'

