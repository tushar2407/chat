from django.shortcuts import render, get_object_or_404
from main.models import Chat, Contact, Message

# Create your views here.

def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    return render(request, 'room.html',{
        'room_name' : room_name
    })

def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id = chatId)
    return chat.messages.all()[:10]

