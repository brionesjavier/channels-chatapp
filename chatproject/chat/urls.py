from django.urls import path
from chat.views import Main, Login, Home, Register, ChatPerson, Logout


urlpatterns = [
	path('',Main.as_view(), name='main'),
    path('login', Login.as_view(), name='login'),
    path('home', Home.as_view(), name='home'),
    path('register', Register.as_view(), name='register'),
    path('chat', ChatPerson.as_view(), name='chat'),
    path('logout', Logout.as_view(), name='logout')
    
]