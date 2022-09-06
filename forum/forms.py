from django import forms
from .models import Answer, Room, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)


class CustiomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

# form for creating new room/question
class CreateNewRoom(forms.Form):
    topic = forms.CharField(label='Topic', max_length=100)
    description = forms.CharField(label='Description', max_length=10000)
    category = forms.CharField(label='Category', max_length=50)
        