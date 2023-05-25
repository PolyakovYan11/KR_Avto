import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe

from main.models import Profiles


def chats(request):
    return render(request, "chat/chat_rooms.html")


@login_required
def room(request, room_name):
    prof = Profiles.objects.get(pk=room_name)
    return render(request, "chat/room.html",
                  {"room_name_json": mark_safe(json.dumps(room_name)),
                   "prof": prof,
                   "username": mark_safe(json.dumps(request.user.email))})
