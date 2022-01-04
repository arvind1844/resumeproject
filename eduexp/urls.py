from django.urls import path
from . import views

urlpatterns = [
    path("eduexp/", views.display_eduexp, name="eduexp")
]
