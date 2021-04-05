from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('make_login/', views.make_login, name='make_login'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('sign-up/', views.SignUp.as_view(), name='sign_up'),
    path('add_user/', views.add_user, name='add_user'),
    path('current_weather/<str:city>/', views.current_weather, name='current_weather')
]
