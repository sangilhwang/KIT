# photo 앱과 관련된 url을 관리

from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_list, name="photo_list"),
    path("photo/<int:pk>/", views.photo_detail, name="photo_detail"), # 127.0.0.1:8000/photo/1/ 주소를 받으면 1 값을 pk로 반환한다
    path("photo/new/", views.photo_post, name="photo_post"),
    path("photo/<int:pk>/edit/", views.photo_edit, name="photo_edit"),
    path("photo/<int:pk>/delete/", views.photo_delete, name="photo_delete"),
]
