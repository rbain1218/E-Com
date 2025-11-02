from django.shortcuts import redirect, get_object_or_404, render
from .models import ChatRoom
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()


def room(request, username):
    receiver = get_object_or_404(User, username=username)
    return render(request, 'chat/room.html', {'receiver': receiver})

@login_required
def start_chat(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    buyer = request.user
    seller = product.seller
    # Try find existing room
    room, created = ChatRoom.objects.get_or_create(buyer=buyer, seller=seller, product=product)
    return redirect('chat:room', room_id=room.id)

@login_required
def room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

from django.shortcuts import render
from django.contrib.auth.models import User

def rooms(request):
    """List all available chat rooms."""
    return render(request, 'chat/rooms.html')

def room(request, username):
    """Open a chat room between current user and the given username."""
    friend = User.objects.get(username=username)
    return render(request, 'chat/room.html', {'friend': friend})
