from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect


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

class UserPostsView(HomeView):
    """User's posts view."""
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


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
    #     form = self.get_form()
    #     if not form.is_valid():
    #         return HttpResponse('error')
    #     form.save(request=request)
    #     return HttpResponseRedirect(self.success_url)

    def post(self, request):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, user=request.user)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, user):
        """ If form is valid save the associated model. """
        self.object = form.save(user=user)
        return HttpResponseRedirect(self.get_success_url())

    # def post(self, request):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     form.instance.author = request.user
    #
    #     if not form.is_valid():
    #         return HttpResponse('All is bad')
    #     form.save(commit=True)
    #     return HttpResponseRedirect(self.success_url)

    # form = self.get_form()
    # if form.is_valid():
    #     return form.save()
    # else:
    #     return self.form_invalid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         form.cleaned_data['author'] = self.request.user
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class PostUpdateView(UpdateView):
    template_name = "core/post_update.html"
    model = Post
    form_class = PostForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('core:post_detail')

    def update(self, request):
        return super().update(request)

    # def post(self, request):
    #     self.object = None
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form, user=request.user)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self, form, user):
    #     """ If form is valid save the associated model. """
    #     self.object = form.save(user=user)
    #     return HttpResponseRedirect(self.get_success_url())






