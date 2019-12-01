from django.urls import path
from .views import PersonView

urlpatterns = [
    path('person/', PersonView.as_view(), name="person"),
]
