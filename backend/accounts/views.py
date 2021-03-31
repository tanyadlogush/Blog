from django.views.generic import CreateView, UpdateView, DetailView
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """User registration view."""
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

    form_class = CustomUserCreationForm
    # form_class = UserCreationForm


# class CustomUserDetailView(DetailView):
#     # TODO: Finish detail view
#     pass
#
# class CustomUserChangeView(UpdateView):
#     # TODO: Finish change view
#     pass
