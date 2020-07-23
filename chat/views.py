from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404
from .models import Message
import json

User = get_user_model()

@login_required
def index(request):
    context_dict = {
        'friends': User.objects.all().exclude(username=request.user.username),
        'user': request.user,
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'index.html', context_dict)

def get_user_contact(username):
    return get_object_or_404(User, username=username)