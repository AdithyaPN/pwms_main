from django.shortcuts import render

# Create your views here.
def collection_dashboard(request):
    return render(request, 'collection/collection_dashboard.html')

def approve_request(request):
    return render(request, 'collection/approve_request.html')

def change_password(request):
    return render(request, 'collection/change_password.html')

def profile(request):
    return render(request, 'collection/collection_profile.html')
