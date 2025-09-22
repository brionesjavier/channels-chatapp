from django.views import View
from django.shortcuts import render


class Register(View):
    def get(self,request):
        return render(request=request, template_name="chat/register.html")