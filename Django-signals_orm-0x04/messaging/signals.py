from django.db.models.signals import post_save
from django.db.models.signals import pre_save
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
    if instance.pk:  # Editing existing message
        try:
            original = Message.objects.get(pk=instance.pk)
            if original.content != instance.content:
                # Save the previous version
                MessageHistory.objects.create(
                    message=original,
                    old_content=original.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass

