from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class MainView(TemplateView):
    template_name = "index.html"


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "home.html", context={"is_staff": request.user.is_staff})
        return HttpResponse("")