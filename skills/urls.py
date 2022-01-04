from django.urls import path
from . import views

urlpatterns = [
    path("skills/", views.display_skills, name="skills"),
]
