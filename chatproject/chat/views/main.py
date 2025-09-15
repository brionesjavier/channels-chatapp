from django.views import View
from django.shortcuts import render

# Create your views here.
class Main(View):
    def get(self, request):
        return render(request,template_name='chat/main.html') 