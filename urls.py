
from django.urls import path
from .import views

urlpatterns = [
    path("", views.hr),
    path("delete/<int:id>/", views.de),
    path("update/<int:id>/", views.up),
    path("update/<int:id>/change/", views.ch),
    path("mark_as_done/<int:id>/", views.mark_as_done)
    ]