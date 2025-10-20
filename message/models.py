from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=100)
    users=models.ManyToManyField(User, related_name="chatroom_users")

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ManyToManyField(User, related_name="message_receivers", blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat_room = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
