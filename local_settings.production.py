import os
from get_docker_secret import get_docker_secret

#####################################
########## Django settings ##########
#####################################
# See <https://docs.djangoproject.com/en/1.9/ref/settings/>
# for more info and help. If you are stuck, you can try Googling about
# Django - many of these settings below have external documentation about them.
#
# The settings listed here are of special interest in configuring the site.

# SECURITY WARNING: keep the secret key used in production secret!
# You may use <http://www.miniwebtool.com/django-secret-key-generator/>
# to generate this key.
SECRET_KEY = get_docker_secret('django_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Change to False once you are done with runserver testing.

# Uncomment and set to the domain names this site is intended to serve.
# You must do this once you set DEBUG to False.
ALLOWED_HOSTS = ['phylactery.gozz.id.au', '*']

# Your database credentials.
# Documentation: <https://docs.djangoproject.com/en/1.9/ref/databases/>
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'phylactery',
        'USER': 'phylactery',
        'PASSWORD': get_docker_secret('postgres_password', safe=False),
        'HOST': 'postgres-prod',
        'PORT': '5432',
    }
}

# Internationalization.
# Documentation: <https://docs.djangoproject.com/en/1.9/topics/i18n/>
LANGUAGE_CODE='en-au'
TIME_ZONE='Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'phylactery/static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'uwaunigames@gmail.com'
EMAIL_HOST_PASSWORD = get_docker_secret('email_password', safe=False)
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'uwaunigames@gmail.com'

# Celery Stuff
CELERY_BROKER_URL = 'redis://redis-prod:6379'
CELERY_RESULT_BACKEND = 'redis://redis-prod:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Australia/Perth'
BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
