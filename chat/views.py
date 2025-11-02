from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Room, Message

User = get_user_model()


@login_required
def rooms(request):
    """Show all users to start chat"""
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/rooms.html', {'users': users})


@login_required
def room(request, username):
    """Open chat room between two users"""
    other_user = get_object_or_404(User, username=username)
    room_name = '_'.join(sorted([request.user.username, other_user.username]))
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=room, user=request.user, content=content)
            return redirect('chat:room', username=other_user.username)

    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages,
        'other_user': other_user
    })
