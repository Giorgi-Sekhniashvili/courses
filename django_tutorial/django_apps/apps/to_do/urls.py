from django.urls import path
from .views import ToDoView, TaskListView

app_name = 'to_do'

urlpatterns = [
    path('', ToDoView.as_view(), name='to_do'),
    path('task_list_view/', TaskListView.as_view(), name='task_list_view')
]
