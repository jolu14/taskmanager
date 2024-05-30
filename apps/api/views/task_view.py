from rest_framework import viewsets
from apps.api.models import Task
from apps.api.serializers import TaskSerializer
from apps.api.utilities.notification import Notification


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        task_data = response.data
 
        notification = Notification(task_data)
        notification.send_email_notification('created')  # Envía la notificación asíncrona


        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        task_data = response.data
 
        notification = Notification(task_data)
        notification.send_email_notification('updated')  # Envía la notificación asíncrona

        return response