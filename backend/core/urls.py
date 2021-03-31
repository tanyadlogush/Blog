from django.urls import path
from .views import AboutView, HomeView, PostDetailView, PostCreateView, PostDeleteView, UserPostsView, PostUpdateView

app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path("post/<int:id>/", PostDetailView.as_view(), name='post_detail'),
    path("post/delete/<int:id>/", PostDeleteView.as_view(), name='post_delete'),
    path("post/user_posts/", UserPostsView.as_view(), name='user_posts_page'),
    path("post/post_update/<int:id>/", PostUpdateView.as_view(), name='post_update'),

]
