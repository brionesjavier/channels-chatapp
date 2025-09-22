from django.shortcuts import render
from django.views import View


class ChatPerson(View):
    def get(self, request):
        return render(request=request, template_name='chat/chat_person.html')