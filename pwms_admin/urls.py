from django.urls import path
from . import views

app_name='pwms_admin'
urlpatterns = [
    path('dashboard',views.admin_dashboard, name='dashboard'),
    path('approveuser',views.approve_user, name='approveuser'),
    path('viewrequest',views.view_request, name='viewrequest'),
    path('notifications',views.notifications, name='notifications'),
    path('addagent',views.add_collection_agent, name='addagent'),
    path('viewagent',views.view_agent, name='viewagent'),
]