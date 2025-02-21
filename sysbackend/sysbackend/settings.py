
from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(^0^mj%ad(j8=t*)kky48w*@u^fohvr%nsz3^b9l@ka%8@n4xm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',  # ¡Añade esta línea!
    'rest_framework_simplejwt.token_blacklist',  # Agrega esta línea
    'djoser',
    'aplicaciones.tareas',
    
    'aplicaciones.autenticacion', #con apis
    'aplicaciones.usuarios',
    'aplicaciones.login',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Debe estar al principio
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Con esto permitimos solicitudes desde esa unicacion
 # Origen de tu frontend React
CORS_ALLOWED_ORIGINS = ['http://localhost:5173']


print(CORS_ALLOWED_ORIGINS)
#Si quieres permitir todos los orígenes (no recomendado en producción), puedes usar:
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'sysbackend.urls'

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

WSGI_APPLICATION = 'sysbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

#BASE DE DATOS POSTGRES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tareas',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Para usuario personalizado
AUTH_USER_MODEL = 'usuarios.usuarios'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#Configuraciones para la autenticacion REST_FRAMEWORK = {
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Usar JWT para autenticación
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Ejemplo: Ajusta la duración del access token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Ejemplo: Ajusta la duración del refresh token
    'ROTATE_REFRESH_TOKENS': False,                 # Ejemplo: Rotación de refresh tokens (opcional)
    'BLACKLIST_TOKEN_AFTER_VERIFY': True,            # ¡Esta línea es CRUCIAL!
}

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'aplicaciones.usuarios.serializers.CustomUserCreateSerializer',  # Serializador en la app usuarios
        'user': 'aplicaciones.usuarios.serializers.CustomUserSerializer',              # Serializador en la app usuarios
    },
    'USER_ID_FIELD': 'id',  # Campo único para identificar al usuario
    'LOGIN_FIELD': 'email',  # Campo usado para iniciar sesión
}