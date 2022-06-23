from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    #Basically requesting for the username that appears at end of url in the website when you enter a room with a user say Tom
    username = request.GET.get('username')

    #Now we want to get the room details
    #we are going to use the name of the room to assess the database
    #We are going to get the particular model that has the name of the room that is got
    room_details = Room.objects.get(name=room)

    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    #if there is an object in this room with the name of this room exists then we want to redirect the user
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    
    #if the room is new
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent Successfully!')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
        
