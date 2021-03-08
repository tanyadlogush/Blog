from django.urls import path
from .views import AboutView, HomeView

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('about/', AboutView.as_view()),
]
