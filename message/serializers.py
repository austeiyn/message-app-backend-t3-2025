from rest_framework.serializers import ModelSerializer
from message.models import Chatroom, Message

class Chat_roomSerializer(ModelSerializer):
    class Meta:
        model = Chatroom
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'