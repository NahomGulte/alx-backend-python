from django.db import models

# Create your models here.

class Chats(models.Model):
    user = models.CharField()
    conversattion = models.CharField(max_length=100)
    message = models.CharField()


    def __str__(self):
        return self.name
