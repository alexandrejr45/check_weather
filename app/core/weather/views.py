from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .services import get_current_weather


class CheckWeather(LoginRequiredMixin, View):

    def get(self, request, city: str):
        try:
            weather = dict(get_current_weather(city))
            print(weather)
            return JsonResponse(weather)
        except Exception as err:
            return err
