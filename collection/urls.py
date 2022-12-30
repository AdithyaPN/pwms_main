from django.urls import path, include
from . import views

app_name='collection'
urlpatterns = [
    path('dashboard',views.collection_dashboard, name='dashboard'),
    path('approve_request',views.approve_request, name='approve_request'),
    path('change_password',views.change_password, name='change_password'),
    path('profile',views.profile, name='profile'),
]
