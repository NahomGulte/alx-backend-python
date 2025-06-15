from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Prefetch
from .models import Message

def get_conversation(user):
    # Top-level messages (not replies)
    messages = Message.objects.filter(
        receiver=user,
        sender=request.user,
        parent_message__isnull=True
    ).select_related('sender').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender'))
    )

    return messages
    
@login_required
def delete_user(request):
    user = request.user
    logout(request)  
    user.delete()
    return redirect('home')  
