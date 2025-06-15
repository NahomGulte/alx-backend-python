from django.db import models
from django.contrib.auth.models import User

class MessageQuerySet(models.QuerySet):
    def unread_for_user(self, user):
        return self.filter(receiver=user, read=False)

class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return MessageQuerySet(self.model, using=self._db)

    def unread_for_user(self, user):
        return self.get_queryset().unread_for_user(user)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False) 

    parent_message = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE
    )
    read = models.BooleanField(default=False)

    objects = models.Manager()
    unread = UnreadMessagesManager() 
    def __str__(self):
        return f"Message {self.id} from {self.sender} to {self.receiver}"
    def is_reply(self):
        return self.parent_message is not None
        
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by=models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    def __str__(self):
        return f"Notification for {self.user} - Message ID {self.message.id}"
