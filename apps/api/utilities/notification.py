from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_celery(task, action):
    subject = f'Task {action.capitalize()}'
    message = f'The task "{task["title"]}" has been {action}.'
    recipient_list = [task["email"]]  
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

class Notification:
    def __init__(self, task_data={}):
        self.task_data = task_data

   
    def send_email_notification(self, action):
        send_email_celery.delay(self.task_data, action)