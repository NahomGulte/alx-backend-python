from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  
        try:
            original = Message.objects.get(pk=instance.pk)
            if original.content != instance.content:
                
                MessageHistory.objects.create(
                    message=original,
                    old_content=original.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()