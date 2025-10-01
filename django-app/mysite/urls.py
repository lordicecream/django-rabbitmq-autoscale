from django.urls import path
from . import views

urlpatterns = [
    path("enqueue/", views.enqueue),
]