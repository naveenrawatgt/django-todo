from django.shortcuts import render

def dashboard(request):
    return render(request, 'list/dashboard.html')