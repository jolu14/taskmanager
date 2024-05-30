# my_project/settings/development.py
from .base import *


DEBUG = True

DEVELOPMENT_INSTALLED_APPS = [
  
]

# Concatinate the local apps to the installed apps list of our base settings
INSTALLED_APPS = INSTALLED_APPS + DEVELOPMENT_INSTALLED_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}