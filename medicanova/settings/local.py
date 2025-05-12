import dj_database_url
from .base import *
from dotenv import load_dotenv


load_dotenv()

DEBUG = True

SECRET_KEY = "abc"

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]


DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://medicanovauser:testtest123@localhost:5432/medicanova",
        conn_max_age=600,
    )
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "w01f4a6a.kasserver.com"
# EMAIL_HOST_USER = "info@medicanova.de"
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = "info@medicanova.de"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]
CORS_ALLOW_ALL_ORIGINS = True  # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_HEADERS = ["*"]

AWS_QUERYSTRING_AUTH = True
