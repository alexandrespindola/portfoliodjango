from pathlib import Path
import os
from decouple import config
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

LOCALHOST = config('LOCALHOST')
HEROKU = config('HEROKU')
CUSTOM_DOMAIN = config('CUSTOM_DOMAIN')

ALLOWED_HOSTS = [
    LOCALHOST,
    CUSTOM_DOMAIN,
    HEROKU
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'portfoliodjango.urls'

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
                #'django.template.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfoliodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

SUPABASE_ENGINE = config('SUPABASE_ENGINE')
SUPABASE_NAME=config('SUPABASE_NAME')
SUPABASE_USER = config('SUPABASE_USER')
SUPABASE_PASSWORD = config('SUPABASE_PASSWORD')
SUPABASE_HOST = config('SUPABASE_HOST')

DATABASES = {
    'default': {
        'ENGINE': SUPABASE_ENGINE,
        'NAME': SUPABASE_NAME,
        'USER': SUPABASE_USER,
        'PASSWORD': SUPABASE_PASSWORD,
        'HOST': SUPABASE_HOST,
        'PORT': '5432',
        'CONN_MAX_AGE': 0, 
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Activate Django-Heroku
django_heroku.settings(locals())