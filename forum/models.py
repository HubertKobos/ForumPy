from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Room(models.Model): # Post on the forum
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=10000) # might change to textfield later
    created_at = models.DateField(auto_now_add=True)
    participants = models.ManyToManyField(User, blank=True)

    def __dict__(self):
        return{self.topic, self.description, self.created_at, self.participants}

class Answer(models.Model): # One single answer in the room
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10000) # might change to textfield later
    # created_add ==> add this later

    def __str__(self):
        return self.answer