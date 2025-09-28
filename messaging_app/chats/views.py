from rest_framework import viewsets, status, filters
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        conversation_id = self.request.query_params.get("conversation_id")
        if conversation_id:
            return Message.objects.filter(conversation_id=conversation_id, conversation__participants=self.request.user)
        return Message.objects.none()

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get("conversation")
        if self.request.user not in conversation.participants.all():
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(sender=self.request.user)

