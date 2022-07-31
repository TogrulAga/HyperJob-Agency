"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from hyperjob.views import MainView, MyLoginView, MySignupView, HomeView
from resume.views import ResumeView, ResumeFormView
from vacancy.views import VacancyView, VacancyFormView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainView.as_view()),
    path("resumes", ResumeView.as_view()),
    path("vacancies", VacancyView.as_view()),
    path("login/", RedirectView.as_view(url="/login")),
    path("login", MyLoginView.as_view()),
    path("logout/", RedirectView.as_view(url="/logout")),
    path("logout", LogoutView.as_view()),
    path("signup/", RedirectView.as_view(url="/signup")),
    path("signup", MySignupView.as_view()),
    path("home", HomeView.as_view()),
    path("resume/new", ResumeFormView.as_view()),
    path("vacancy/new", VacancyFormView.as_view()),
]
