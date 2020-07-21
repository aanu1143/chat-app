from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact
import json

User = get_user_model()

@login_required
def index(request, chat_id):
    context_dict = {
        'chat_id': mark_safe(json.dumps(chat_id)),
        'friends': Contact.objects.all().exclude(user__username=request.user.username),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'index.html', context_dict)

@login_required
def room(request, chat_id):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(chat_id)),
        'username': mark_safe(json.dumps(request.user.username)),
    })


def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('timestamp').all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)