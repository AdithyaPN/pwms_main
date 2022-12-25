from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    return render(request, 'pwms_admin/admin_dashboard.html')

def approve_user(request):
    return render(request, 'pwms_admin/user_approval.html')

def view_request(request):
    return render(request, 'pwms_admin/view_request.html')
