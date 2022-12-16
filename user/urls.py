from django.urls import path
from . import views

app_name='user'
urlpatterns = [
    path('home',views.user_home, name='Home'),
    path('login',views.user_login, name='login'),
    path('user_request',views.user_request, name='user_request'),
    path('news_updates',views.news_updates, name='news_updates'),
]