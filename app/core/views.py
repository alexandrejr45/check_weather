from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.views import View
from .forms import CreateUserForm
from .weather.services import get_current_weather


class Index(LoginRequiredMixin, TemplateView):
    login_url = 'core:login'
    template_name = 'core/index.html'


class Login(auth_views.LoginView):
    template_name = 'core/login.html'


class Logout(auth_views.LogoutView):
    next_page = 'core:index'


class SignUp(View):
    form_class = CreateUserForm
    template_name = 'core/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                user = get_user_model()
                new_user = user.objects.create_user(
                    username=form.cleaned_data['login'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password_check']
                )
                new_user.first_name = form.cleaned_data['first_name']
                new_user.last_name = form.cleaned_data['last_name']
                new_user.save()
                return redirect('core:login')
            except Exception as err:
                return err
                #return HttpResponseBadRequest('Requisição inválida')

        return render(request, self.template_name, {'form': form})


class CheckWeather(LoginRequiredMixin, View):

    def get(self, request, city: str):
        try:
            weather = dict(get_current_weather(city))
            print(weather)
            return JsonResponse(weather)
        except Exception as err:
            return err
