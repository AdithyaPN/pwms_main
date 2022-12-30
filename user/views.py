from django.shortcuts import render

# Create your views here.
def user_home(request):
    return render(request, 'user/home.html')

def user_registration(request):
    return render(request, 'user/user_registration.html')

def user_login(request):
    return render(request, 'user/login.html')

def user_request(request):
    return render(request, 'user/user_request.html')

def news_updates(request):
    return render(request, 'user/news_updates.html')

def user_profile(request):
    return render(request, 'user/user_profile.html')

def change_password(request):
    return render(request, 'user/change_password.html')