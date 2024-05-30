from rest_framework import viewsets
from apps.api.models import Task
from apps.api.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer