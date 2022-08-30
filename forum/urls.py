from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name="forum"

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home_page"),
    path('room/<int:pk>/', views.RoomPageView.as_view(), name="room_page"),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('delete_message/<str:pk>', views.DeleteMessage.as_view(), name='delete_message'),
]