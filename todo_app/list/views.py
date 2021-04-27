from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Activity

class DashBoardView(TemplateView):
    template_name = 'list/dashboard.html'

class ToDoListView(ListView):
    model = Activity
    paginate_by = 10