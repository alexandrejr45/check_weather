from django.urls import path
from . import views as core_views
from .weather import views as weather_views


app_name = 'core'


urlpatterns = [
    path('', core_views.Index.as_view(), name='index'),
    path('login/', core_views.Login.as_view(), name='login'),
    path('logout/', core_views.Logout.as_view(), name='logout'),
    path('sign-up/', core_views.SignUp.as_view(), name='sign_up'),
    path('weather/<str:city>/', weather_views.CheckWeather.as_view(), name='current_weather')
]
