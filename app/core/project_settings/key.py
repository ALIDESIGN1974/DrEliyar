import os

SECRET_KEY = (
    os.getenv("DJANGO_SECRET_KEY")
    or os.getenv("SECRET_KEY")
    or "dev-secret-key"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (
    os.getenv("DJANGO_DEBUG", os.getenv("DEBUG", "1"))
    == "1"
)

ALLOWED_HOSTS = (
    os.getenv("DJANGO_ALLOWED_HOSTS")
    or os.getenv("ALLOWED_HOSTS")
    or "*"
).split(",")

CSRF_TRUSTED_ORIGINS = (
    os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS")
    or os.getenv("CSRF_TRUSTED_ORIGINS")
    or ""
).split(",")

CSRF_COOKIE_SECURE = (
    os.getenv("DJANGO_CSRF_COOKIE_SECURE", os.getenv("CSRF_COOKIE_SECURE", "0"))
    == "1"
)

CSRF_COOKIE_HTTPONLY = (
    os.getenv("DJANGO_CSRF_COOKIE_HTTPONLY", os.getenv("CSRF_COOKIE_HTTPONLY", "0"))
    == "1"
)

CSRF_COOKIE_SAMESITE = (
    os.getenv("DJANGO_CSRF_COOKIE_SAMESITE")
    or os.getenv("CSRF_COOKIE_SAMESITE")
    or "Lax"
)