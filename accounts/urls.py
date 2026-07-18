from django.urls import path

from . import views

urlpatterns = [
    path("", views.account_list, name="account_list"),
    path("create/", views.account_create, name="account_create"),
    path("<int:pk>/edit/", views.account_update, name="account_update"),
    path("<int:pk>/", views.account_detail, name="account_detail"),
    path("<int:pk>/archive/", views.account_archive, name="account_archive"),
]
