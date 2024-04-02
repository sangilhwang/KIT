from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("post/", views.post_list),
    path("post/<int:post_id>/", views.post_detail),
    path("post/add/", views.post_add)
]