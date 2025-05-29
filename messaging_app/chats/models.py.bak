from django.contrib.auth.models import AbstractUser 
import uuid
from django.db import models

# Create your models here.

class Chats(AbstractUser):
    first_name=models.CharField(max_length=15, blank=True, null=True)
    last_name=models.CharField(max_length=15, blank=True, null=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField()
    conversattion = models.CharField(max_length=100)
    message = models.CharField()


    def __str__(self):
        return self.name
