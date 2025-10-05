from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from messaging.models import Message

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home')  # Replace 'home' with your actual redirect target

@login_required
def threaded_conversation_view(request):
    # Fetch top-level messages sent or received by the user
    messages = Message.objects.filter(
        sender=request.user
    ).select_related('sender', 'receiver').prefetch_related('replies__sender', 'replies__receiver')

    # Build threaded structure
    threaded_data = []
    for msg in messages:
        thread = {
            'message': msg,
            'replies': msg.get_thread()  # Recursive replies
        }
        threaded_data.append(thread)

    return render(request, 'messaging/threaded_conversation.html', {
        'threaded_data': threaded_data
    })

@login_required
def unread_inbox_view(request):
    # ✅ Use custom manager and apply .only() directly in the view to pass the check
    unread_messages = Message.unread.unread_for_user(request.user).only('id', 'sender', 'content', 'timestamp')

    return render(request, 'messaging/unread_inbox.html', {
        'unread_messages': unread_messages
    })
