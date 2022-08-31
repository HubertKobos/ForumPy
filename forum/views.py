from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import AnswerModelForm, CustiomUserCreationForm
from .models import Answer, Room, User, Friend_Request
from django.shortcuts import render
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = "forum/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Room.objects.all()[:6]
        return context

class FindPeopleView(TemplateView):
    template_name = "forum/find_people_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_users'] = User.objects.all()
        context['all_friend_requests'] = Friend_Request.objects.filter(to_user=self.request.user)
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

@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user=from_user, to_user=to_user
    )
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')
    
@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.tu_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')
    
@login_required
def logout_view(request):
    logout(request)
    # return reverse('forum:logout')