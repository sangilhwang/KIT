from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="post_list"),
    path("<int:post_id>/", views.single_post_page, name="post_detail"),
]
