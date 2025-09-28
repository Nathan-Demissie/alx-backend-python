from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to:
    - Allow only authenticated users
    - Allow only participants of a conversation to send, view, update, and delete messages
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return request.user in obj.conversation.participants.all()
        return request.user in obj.conversation.participants.all


class IsOwnerOrParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        # For messages
        if hasattr(obj, 'sender'):
            return obj.sender == request.user or request.user in obj.conversation.participants.all()
        # For conversations
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        return False
