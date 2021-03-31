from django.urls import path
from .views import SignUpView


app_name = 'accounts'

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('signup/', SignUpView.as_view(), name='signup'),
]