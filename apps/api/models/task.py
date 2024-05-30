from django.db import models
from .base_model import BaseModel

class Task(BaseModel):

    title = models.CharField(null=True, max_length=256) 
    email = models.EmailField(null=True) 
    description = models.CharField(null=True, max_length=256) 

