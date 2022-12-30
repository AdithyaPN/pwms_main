from django.urls import path
from . import views

app_name='user'
urlpatterns = [
    path('home',views.user_home, name='Home'),
    path('registration',views.user_registration, name='registration'),
    path('login',views.user_login, name='login'),
    path('user_request',views.user_request, name='user_request'),
    path('news_updates',views.news_updates, name='news_updates'),
    path('profile',views.user_profile, name='profile'),
    path('change_password',views.change_password, name='change_password'),
]