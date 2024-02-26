"""
Application config.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DJANGO_DEBUG", 1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")


# Application definition

INSTALLED_APPS = []

MIDDLEWARE = []

ROOT_URLCONF = "google_calendar_clone.urls"

WSGI_APPLICATION = "google_calendar_clone.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
    }
}


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
