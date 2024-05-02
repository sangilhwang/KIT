from django.urls import path
from example.views import helloAPI

urlpatterns = [
    path("hello/", helloAPI),
]