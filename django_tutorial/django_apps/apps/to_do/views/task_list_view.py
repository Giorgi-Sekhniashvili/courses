from django.http import JsonResponse
from django.views.generic import View

from ..models import Task
from ..serializers import TaskSerializer


class TaskListView(View):
    def get(self, request):
        if request.is_ajax():
            tasks = Task.objects.all()

            serializer = TaskSerializer(tasks, many=True)
            return JsonResponse({'data': serializer.data})
        else:
            return JsonResponse({'data': [None]})

    def post(self, request):
        pass
