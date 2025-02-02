from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect 

# Create your views here.
def index(request):
    return render(request, "home/index.html", {})

def donate(request):
    return render(request, "home/donate.html", {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home:index"))

class login(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            return reverse_lazy('edu:index')
        return reverse_lazy('home:index')