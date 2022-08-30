from urllib import request
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from .forms import AnswerModelForm, CustiomUserCreationForm
from .models import Answer, Room
from django.shortcuts import render
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = "forum/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Room.objects.all()[:6]
        return context

class RoomPageView(CreateView):
    template_name = "forum/room_page.html"
    form_class = AnswerModelForm

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(room=pk) # use filter instead of get cause get only one object
        context['room_info'] = Room.objects.get(pk=pk)
        print("context -->", context)
        print("request -->", self.request)
        return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        room = Room.objects.get(pk=pk)
        answer = form.save(commit=False)
        answer.author = self.request.user
        answer.room = room
        answer.save()
        return super(RoomPageView, self).form_valid(form)

    def get_success_url(self):
        return reverse("forum:room_page", args=[self.kwargs['pk']])

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustiomUserCreationForm

    def get_success_url(self):
        return reverse('forum:login')

class DeleteMessage(DeleteView):
    # template_name = "forum/answer_confirm_delete.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        # return reverse('room_page', args=[pk])
        return reverse('forum:home_page')

    def get_queryset(self):
        pk = self.kwargs["pk"]
        asd = Answer.objects.filter(pk=pk)
        print(pk)
        return Answer.objects.filter(id=pk)