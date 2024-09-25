from django.contrib import admin
from django.urls import path, include

from . import views


app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),


    path("comment/<int:pk>", views.comment, name="comment"),
    path("comment_delete/<int:post_pk>/<int:comment_pk>/", views.comment_delete, name="comment_delete"),

    path("like/<int:pk>/", views.like, name="like"),
]