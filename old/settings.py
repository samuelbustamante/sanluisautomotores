PREPEND_WWW = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2',
        'NAME': 'pydevelopers_sanluisautomotores',
        'USER': 'pydevelopers_sanluisautomotores',
        'PASSWORD': '0b2ee2e1',
        'HOST': 'web213.webfaction.com',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = '/home/pydevelopers/webapps/sanluisautomotores_media/'

MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/pydevelopers/webapps/sanluisautomotores_static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l^x7q@%ea%w-cj+=xg%o^++$ce*i!zqaze-ygu=o8s76z#rk4+'

# List of callables that know how to import templates from various sources.
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
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATE_DIRS = (
    '/home/pydevelopers/webapps/sanluisautomotores/myproject/templates/',
)

AUTH_PROFILE_MODULE = 'profile.Profile'
LOGIN_URL = '/registracion/ingresar/'
LOGIN_REDIRECT_URL = '/perfil/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    'myproject.registration',
    'myproject.vehicles',
    'myproject.profile',
    'myproject.home',
    'myproject.contact',
    #'myproject.ads',
    #'myproject.logs',
    #'myproject.cash',
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'pydevelopers'
EMAIL_HOST_PASSWORD = '8d1f37b5'
SERVER_EMAIL = 'no-reply@sanluisautomotores.com'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
