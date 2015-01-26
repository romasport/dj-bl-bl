"""
Django settings for bdlol project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qsexh@lz*k69=&ycwag2!-#9549z&@g)!$5u1u+5xobp^e#yzg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

PROJECT_PATH =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
    PROJECT_PATH + '/perl/templates',
)

MEDIA_ROOT = PROJECT_PATH + "/media"


STATICFILES_DIRS = (
    ('static', PROJECT_PATH + '/static')
)


STATIC_URL = '/static/'

MEDIA_URL = "/media/"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perl',
    'news',
    'users',
    'robots_txt',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bdlol.urls'

WSGI_APPLICATION = 'bdlol.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'bdlol.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


### AUTH: BEGIN
LOGIN_URL = '/users/login/'
LOGIN_ERROR_URL = LOGIN_URL
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

OPENID_SREG = {"required": "nickname, email", "optional": "postcode, country", "policy_url": ""}
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email", "count": 1, "required": True, "alias": "email"},
             {"type_uri": "fullname", "count": 1, "required": False, "alias": "fullname"}]

TWITTER_CONSUMER_KEY = 'see production settings'
TWITTER_CONSUMER_SECRET = 'see production settings'
### AUTH: END

AUTH_USER_MODEL = 'users.User'

### BEGIN SEO

ROBOTS_CACHE_TIMEOUT = 60*60*24

### END SEO