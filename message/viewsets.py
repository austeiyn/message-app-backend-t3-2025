from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from message.models import Chatroom, Message
from message.serializers import Chat_roomSerializer, MessageSerializer


class Chat_roomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chatroom.objects.all()
    serializer_class = Chat_roomSerializer

    def get_queryset(self):
        chatrooms = Chatroom.objects.filter(self.request.user_in_users)
        return chatrooms

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer