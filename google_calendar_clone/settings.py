"""
Application config.
"""

import os
from pathlib import Path
from typing import List

from corsheaders.defaults import default_headers
from supertokens_python import get_all_cors_headers

from google_calendar_clone.auth import init_auth

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Init auth

init_auth()


# Quick-start development settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DJANGO_DEBUG", 1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")


# CORS

CORS_ORIGIN_WHITELIST = [os.environ.get("FRONTEND_URL")]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [os.environ.get("FRONTEND_URL")]

CORS_ALLOW_HEADERS: List[str] = (
    list(default_headers) + ["Content-Type"] + get_all_cors_headers()
)


# Application definition

INSTALLED_APPS = ["corsheaders", "supertokens_python"]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "supertokens_python.framework.django.django_middleware.middleware",
]

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
