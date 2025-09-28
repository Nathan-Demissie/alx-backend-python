from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to:
    - Allow only authenticated users
    - Allow only participants of a conversation to interact with messages
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # For Message objects: check if user is a participant in the conversation
        if hasattr(obj, 'conversation') and hasattr(obj.conversation, 'participants'):
            return request.user in obj.conversation.participants.all()
        return False



class IsOwnerOrParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        # For messages
        if hasattr(obj, 'sender'):
            return obj.sender == request.user or request.user in obj.conversation.participants.all()
        # For conversations
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        return False
