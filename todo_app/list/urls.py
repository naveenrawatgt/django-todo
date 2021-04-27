from django.urls import path
from .views import DashBoardView, ToDoListView

app_name = 'list'

urlpatterns = [
    path('todo', DashBoardView.as_view(), name='todo'), 
    path('todo-items', ToDoListView.as_view(), name='todo-items')
]