from pathlib import Path
import environ
from SmartChild_backend.constants import DB_HOST_ENV, DB_NAME_ENV, DB_PASSWORD_ENV, DB_PORT_ENV, DB_USER_ENV, FIREBASE_API_KEY_ENV, FIREBASE_APP_ID_ENV, FIREBASE_AUTH_DOMAIN_ENV, FIREBASE_MESSAGING_SENDER_ID_ENV, FIREBASE_PROJECT_ID_ENV, FIREBASE_STORAGE_BUCKET_ENV, SECRET_KEY_ENV

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env() 

FIREBASE_API_KEY = env(FIREBASE_API_KEY_ENV)
FIREBASE_AUTH_DOMAIN = env(FIREBASE_AUTH_DOMAIN_ENV)
FIREBASE_PROJECT_ID = env(FIREBASE_PROJECT_ID_ENV)
FIREBASE_STORAGE_BUCKET = env(FIREBASE_STORAGE_BUCKET_ENV)
FIREBASE_MESSAGING_SENDER_ID = env(FIREBASE_MESSAGING_SENDER_ID_ENV)
FIREBASE_APP_ID = env(FIREBASE_APP_ID_ENV)
SECRET_KEY = env(SECRET_KEY_ENV)

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SmartChild_backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'SmartChild_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env(DB_NAME_ENV),
        'USER': env(DB_USER_ENV),
        'PASSWORD': env(DB_PASSWORD_ENV),
        'HOST': env(DB_HOST_ENV, default='localhost'),
        'PORT': env(DB_PORT_ENV, default='5432'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
