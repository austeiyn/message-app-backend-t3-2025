from django.contrib import admin

from message.models import Chatroom, Message

# Register your models here.
admin.site.register(Chatroom)
admin.site.register(Message)
