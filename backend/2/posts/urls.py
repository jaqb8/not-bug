from django.urls import path
from posts import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_post, name="create-post"),
    path("post/<int:id>", views.post_detail, name="post-detail"),
    path("post/<int:id>/edit", views.post_edit, name="post-edit"),
]
