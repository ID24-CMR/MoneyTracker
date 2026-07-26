from django.urls import path

from . import views

urlpatterns = [
    path("", views.budget_list, name="budget_list"),
    path("new/", views.budget_create, name="budget_create"),
]
