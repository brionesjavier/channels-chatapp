from django.views import View


class Logout(View):
    def get(self, request):
        return None