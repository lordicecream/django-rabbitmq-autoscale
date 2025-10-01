import os

SECRET_KEY = "dummy"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
]

MIDDLEWARE = []
ROOT_URLCONF = "mysite.urls"

# Optional: if you keep staticfiles app
STATIC_URL = "/static/"
