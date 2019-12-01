from django.urls import path
from .views import LoginView, RegisterUsers, ElasticsearchView


urlpatterns = [
    path('login/', LoginView.as_view(), name="auth-login"),
    path('register/', RegisterUsers.as_view(), name="auth-register"),
    path('elasticsearch/', ElasticsearchView.as_view(), name="elasticsearch"),
]
