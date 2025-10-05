from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory  # ✅ Make sure MessageHistory is imported

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id is None:
        return  # Skip new messages

    try:
        old_instance = Message.objects.get(id=instance.id)
    except Message.DoesNotExist:
        return

    if old_instance.content != instance.content:
        MessageHistory.objects.create(  # ✅ Required for the check
            message=old_instance,
            old_content=old_instance.content
        )
        instance.edited = True
