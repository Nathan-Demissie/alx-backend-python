from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from messaging.models import Message

@cache_page(60)  # ✅ Cache this view for 60 seconds
@login_required
def conversation_list_view(request):
    # Fetch all messages involving the user
    messages = Message.objects.filter(
        receiver=request.user
    ).select_related('sender', 'receiver').order_by('-timestamp')

    return render(request, 'chats/conversation_list.html', {
        'messages': messages
    })
