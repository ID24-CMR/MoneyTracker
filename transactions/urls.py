from django.urls import path
from . import views
urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),
    path("create/", views.transaction_create, name="transaction_create"),
    path("<int:pk>/", views.transaction_detail, name="transaction_details"),
    path("<int:pk>/edit", views.transaction_update, name="transaction_update"),
    path("<int:pk>/update", views.transaction_archive, name="transaction_archive"),
]