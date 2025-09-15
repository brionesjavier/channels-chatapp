from django.urls import path
from chat.views import Main


urlpatterns = [
	path('',Main.as_view() ,name='main')
]