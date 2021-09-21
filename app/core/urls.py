from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('sign-up/', views.SignUp.as_view(), name='sign_up'),
    path('current_weather/<str:city>/', views.CheckWeather.as_view(), name='current_weather')
]
