# auth_app/urls.py
from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view()),  # URL pattern without the trailing slash
]

