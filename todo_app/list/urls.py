from django.urls import path
from .views import dashboard

app_name = 'list'

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),    
]