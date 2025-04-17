from .base import *  # noqa: F401, F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # noqa: F811

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*5ol0*m=n%@q6&yzmd*e^ftp+j+nv@w!-f9f_fgp93j)xez)0z"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
