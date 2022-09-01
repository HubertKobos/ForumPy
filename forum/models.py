from venv import create
from django.db.models.signals import post_save, post_delete
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)
    number_of_questions = models.IntegerField(default=0)
    number_of_answers = models.IntegerField(default=0)

class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)

class Room(models.Model): # Post on the forum
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="created_by")
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=10000) # might change to textfield later
    created_at = models.DateField(auto_now_add=True)
    participants = models.ManyToManyField(User, blank=True)
    number_of_answers = models.IntegerField(default=0)
    category = models.CharField(max_length=50, null=True, blank=True)

    # def __dict__(self):
    #     return{self.topic, self.description, self.created_at, self.participants}

class Answer(models.Model): # One single answer in the room
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10000) # might change to textfield later
    # created_add ==> add this later

    def __str__(self):
        return self.answer

#updates number of answers user wrote
def post_answer_created_signal(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(id=instance.author.id)
        number_of_answers = user.number_of_answers
        number_of_answers = number_of_answers + 1
        User.objects.filter(id=instance.author.id).update(number_of_answers=number_of_answers)
post_save.connect(post_answer_created_signal, sender=Answer)

# updates number of answers user wrote
def post_answer_delete_signal(sender, instance, **kwargs):
    user = User.objects.get(id=instance.author.id)
    number_of_answers = user.number_of_answers
    number_of_answers = number_of_answers - 1
    User.objects.filter(id=instance.author.id).update(number_of_answers=number_of_answers)
post_delete.connect(post_answer_delete_signal, sender=Answer)

# updates nubmer of questions user created
def post_question_created_signal(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(id=instance.created_by.id)
        number_of_questions = user.number_of_questions
        number_of_questions = number_of_questions + 1
        User.objects.filter(id=instance.created_by.id).update(number_of_questions=number_of_questions)
post_save.connect(post_question_created_signal, sender=Room)

# updates nubmer of questions user created
def post_question_delete_signal(sender, instance, **kwargs):
    user = User.objects.get(id=instance.created_by.id)
    number_of_questions = user.number_of_questions
    number_of_questions = number_of_questions - 1 
    User.objects.filter(id=instance.created_by.id).update(number_of_questions=number_of_questions)
post_delete.connect(post_question_delete_signal, sender=Room)

# increase number of answers in the room to render information on the main page
def post_number_of_answers_created_signal(sender, created, instance, **kwargs):
    if created:
        created_answer_room = Room.objects.get(id=instance.room.id)
        number_of_answers = created_answer_room.number_of_answers
        number_of_answers = number_of_answers + 1
        Room.objects.filter(id=instance.room.id).update(number_of_answers=number_of_answers)

post_save.connect(post_number_of_answers_created_signal, sender=Answer)

# decrease number of answers in the room to render information on the main page
def post_number_of_answers_delete_signal(sender, instance, **kwargs):
    created_answer_room = Room.objects.get(id=instance.room.id)
    number_of_answers = created_answer_room.number_of_answers
    number_of_answers = number_of_answers - 1 
    Room.objects.filter(id=instance.room.id).update(number_of_answers=number_of_answers)

post_delete.connect(post_number_of_answers_delete_signal, sender=Answer)