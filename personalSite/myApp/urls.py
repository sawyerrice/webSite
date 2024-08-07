from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("myApp/projects", views.projects, name = "projects"),
    path("myApp/education", views.education, name = "edu"),
    path("myApp/work", views.work, name = "work")
]