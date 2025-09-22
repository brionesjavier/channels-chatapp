from django.views import View
from django.shortcuts import render


class Login(View):
    def get(self,request):
        return render(request=request, template_name="chat/login.html")
    