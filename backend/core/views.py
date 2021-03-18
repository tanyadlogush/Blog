from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm


# posts = [
#     {'title': 'How to learn VIM', 'author': 'W. Vincent', 'data': '12315'},
#     {'title': 'How to learn Python', 'author': 'Guido van Rossum', 'data': '123145'},
#     {'title': 'How to learn Rust', 'author': 'Fedor', 'data': '1234515'},
# ]

class HomeView(ListView):
    """Base home view."""
    template_name = 'core/home.html'
    queryset = Post.objects.all().order_by('-updated_at')  # order_by('title')
    # queryset = Post.objects.values('title', 'body', 'image')


class AboutView(TemplateView):
    """Base about view."""
    template_name = 'core/about.html'


class PostDetailView(DetailView):
    template_name = "core/post_detail.html"
    model = Post
    pk_url_kwarg = "id"


class PostDeleteView(DeleteView):
    template_name = "core/post_delete.html"
    model = Post
    pk_url_kwarg = "id"
    success_url = reverse_lazy('core:home_page')


class PostCreateView(CreateView):
    template_name = "core/post_create.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('core:home_page')

    # def post(self, request):
    #     return super().post(request)
