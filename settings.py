PREPEND_WWW = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sanluisautomotores.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Argentina/San_Luis'
LANGUAGE_CODE = 'es-AR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = '/home/pydevelopers/webapps/sanluisautomotores_media'
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
SECRET_KEY = '=zz0!)+!hbyp+6^p=mqg=!j79-9m83oc!@e0^)90+j%*7j08=l'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'
TEMPLATE_DIRS = (
    '/home/pydevelopers/webapps/sanluisautomotores/myproject/myproject/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'myproject.registration',
    'myproject.vehicles',
    'myproject.profile',
    'myproject.contact',
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'pydevelopers'
EMAIL_HOST_PASSWORD = '8d1f37b5'
SERVER_EMAIL = 'no-reply@sanluisautomotores.com'
LOGIN_URL = '/registrarse/'
LOGIN_REDIRECT_URL = '/publicar/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
