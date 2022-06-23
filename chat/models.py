from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    #name is the name of the chatroom to be entered which can have max length of 1000 characters
    name = models.CharField(max_length=1000)

class Message(models.Model):
    #value is the message the user wants to send in the chatroom
    value = models.CharField(max_length=10000000)
    #datetime field should have datetime imported
    #datetime does not have any max length, instead has default value
    #The default value is datetime.now which is currrent date taken as default value
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000000)
    room = models.CharField(max_length=10000000)
    #we can also use foreign key to link the room field of message model to model room