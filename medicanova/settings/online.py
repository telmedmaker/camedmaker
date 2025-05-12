import os
from .base import *
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ["localhost", "medicanova.de", "www.medicanova.de"]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DBNAME"),
        "HOST": os.environ.get("DBHOST"),
        "USER": os.environ.get("DBUSER"),
        "PASSWORD": os.environ.get("DBPASS"),
        "OPTIONS": {"sslmode": "require"},
    }
}

SECURE_SSL_REDIRECT = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "w01f4a6a.kasserver.com"
EMAIL_HOST_USER = "info@medicanova.de"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@medicanova.de"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
