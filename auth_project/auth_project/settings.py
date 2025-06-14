"""
Django settings for auth_project project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6#^=^kz!#s6ih^%0seyn46$m0+d=e46ice_k2ja4ojv^*ymm4a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'django.contrib.staticfiles',
    'accounts',
    'django.contrib.messages',
]

# Custom user parameters
SITE_ID = 1
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_URL = '/accounts/login/'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
     'django.contrib.messages.middleware.MessageMiddleware',
    'accounts.conteoMiddleware.LastSeenMiddleware',
]
"""
Aquí algunos de los middlewares más comunes e importantes:

Middleware	Función
-----------------------
SecurityMiddleware  → 	Aplica medidas de seguridad como redirección a HTTPS, cabeceras seguras, etc.
SessionMiddleware  → 	Habilita el uso de sesiones con cookies.
CommonMiddleware  → 	Agrega cabeceras comunes, redirecciona si falta /, etc.
CsrfViewMiddleware  → 	Protege contra ataques CSRF en formularios.
AuthenticationMiddleware  → 	Agrega request.user y permite saber si alguien está autenticado.
MessageMiddleware  → 	Permite usar el sistema de mensajes (messages) en vistas y templates.
XFrameOptionsMiddleware  → 	Evita que tu sitio sea embebido en un iframe (protección contra clickjacking).

corsheaders.middleware.CorsMiddleware → para habilitar CORS.

debug_toolbar.middleware.DebugToolbarMiddleware → para depurar tu app en desarrollo.

whitenoise.middleware.WhiteNoiseMiddleware → para servir archivos estáticos en producción (muy usado con Heroku).
"""

ROOT_URLCONF = "auth_project.urls"
import os
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
         'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'django.contrib.messages.context_processors.messages',
]
WSGI_APPLICATION = "auth_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

#LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = 'es'

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
