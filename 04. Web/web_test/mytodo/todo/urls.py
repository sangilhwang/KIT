from django.contrib import admin
from django.urls import path, include
from todo import views

app_name = "todo"
urlpatterns = [
    path("", views.todo),
    path("<int:todo_id>/", views.todo_detail)
]
