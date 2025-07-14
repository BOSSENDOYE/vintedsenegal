from rest_framework import serializers
from .models import Message, Conversation

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'content', 'timestamp']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'subject', 'participants', 'created_at', 'messages']

class SendMessageSerializer(serializers.Serializer):
    recipient_id = serializers.IntegerField()
    content = serializers.CharField()
    subject = serializers.CharField(required=False, allow_blank=True)
