from django.urls import path, include
from . import views

app_name='collection'
urlpatterns = [
    path('dashboard',views.collection_dashboard, name='dashboard'),
]
