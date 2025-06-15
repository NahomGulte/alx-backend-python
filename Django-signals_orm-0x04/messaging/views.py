from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Prefetch
from .models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def inbox(request):
    user = request.user
    unread_messages = Message.unread.unread_for_user(user).only('id', 'sender', 'content', 'timestamp')
    return render(request, 'inbox.html', {'unread_messages': unread_messages})
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
    
@cache_page(60)  
@login_required
def conversation_view(request):
    user = request.user
    messages = Message.objects.filter(receiver=user, parent_message__isnull=True).select_related('sender')
    return render(request, 'conversation.html', {'messages': messages})