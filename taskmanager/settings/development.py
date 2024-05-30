# my_project/settings/development.py
from .base import *

SECRET_KEY="django-insecure-9gwl8nz82e3y8qxmgg-=863#r0#w8$x9dzs8_#&&9o4adiir-="
DEBUG = True

DEVELOPMENT_INSTALLED_APPS = [

]

# Concatinate the local apps to the installed apps list of our base settings
INSTALLED_APPS = INSTALLED_APPS + DEVELOPMENT_INSTALLED_APPS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}