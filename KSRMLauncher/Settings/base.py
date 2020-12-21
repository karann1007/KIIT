
import os
from decouple import config
BASE_DIR = os.path.dirname(
           os.path.dirname(
           os.path.dirname(
           os.path.abspath(__file__))))
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')


SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'EventRestService',
    'corsheaders',
    'knox',
    'Accounts'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'Exceptions.middleware.exception_handler_middleware.ExceptionHandlerMiddleware'

]

ROOT_URLCONF = 'KSRMLauncher.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'KSRMLauncher.wsgi.application'







AUTHENTICATION_BACKENDS = (
    'EventRestService.AuthBackend.CustomUserModelBackend.CustomUserModelBackend',
    'django.contrib.auth.backends.ModelBackend' ,
)


CUSTOM_USER_MODEL = 'Accounts.Models.UserDetails.UserDetails'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CORS_ORIGIN_ALLOW_ALL = True



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ]
}
