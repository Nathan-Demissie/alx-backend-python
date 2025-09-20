from rest_framework import viewsets, status, filters
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and sending messages to conversations.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

