from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name="forum"

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home_page"),
    path('room/<int:pk>/', views.RoomPageView.as_view(), name="room_page"),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('create_new_post/', views.create_new_question, name='create_post'),
    path('delete_message/<str:pk>', views.DeleteMessage.as_view(), name='delete_message'),
    path('find_people/', views.FindPeopleView.as_view(), name='find_people'),
    path('send_friend_request/<int:userID>/',views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestId>/',views.accept_friend_request, name='accept_friend_request'),
    path('logout/', LogoutView.as_view(), name='logout')
]