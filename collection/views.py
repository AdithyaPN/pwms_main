from django.shortcuts import render

# Create your views here.
def collection_dashboard(request):
    return render(request, 'collection/collection_dashboard.html')
