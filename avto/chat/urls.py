from django.urls import path

from . import views

urlpatterns = [
    path("", views.chats, name="chats"),
    path("<str:room_name>", views.room, name="room"),
]
