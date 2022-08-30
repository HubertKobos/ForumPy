from django import forms
from .models import Answer, User
from django.contrib.auth.forms import UserCreationForm

class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)


class CustiomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)