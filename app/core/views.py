from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, RedirectView
from .open_weather_api.services import get_current_weather


class Index(LoginRequiredMixin, TemplateView):
    login_url = 'core:login'
    template_name = 'core/index.html'


class Login(auth_views.LoginView):
    template_name = 'core/login.html'


class Logout(auth_views.LogoutView):
    next_page = 'core:index'


class SignUp(TemplateView):
    template_name = 'core/sign_up.html'

# def index(request):
#     return render(request, 'core/index.html')


@csrf_protect
def add_user(request):
    return HttpResponse(request, 'add user test')


@login_required(login_url='core:login')
def current_weather(request, city: str):
    if request.method == 'GET':
        weather = dict(get_current_weather(city))
        print(weather)
        print(type(weather))
        return JsonResponse(weather)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('core:index')
    else:
        return render(request, 'core/login.html')


