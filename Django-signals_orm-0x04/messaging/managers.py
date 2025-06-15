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
