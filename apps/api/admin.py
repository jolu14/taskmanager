from django.contrib import admin
from django.apps import apps

# Retrive api models
app_models = apps.get_app_config('apps.api').get_models()

# Register API models on admin panel
for model in app_models:
    admin.site.register(model)