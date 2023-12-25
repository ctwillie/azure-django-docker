import os

from .base import *

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
website_hostname = os.environ.get('WEBSITE_HOSTNAME')
env_has_website_hostname = website_hostname is not None

ALLOWED_HOSTS = [website_hostname] if env_has_website_hostname else []
CSRF_TRUSTED_ORIGINS = ['https://' + website_hostname] if env_has_website_hostname else []
DEBUG = True

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # whitenoise: add after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('AZURE_MYSQL_NAME'),
        'HOST': os.environ.get('AZURE_MYSQL_HOST'),
        'USER': os.environ.get('AZURE_MYSQL_USER'),
        'PASSWORD': os.environ.get('AZURE_MYSQL_PASSWORD'),
    }
}

CACHES = {
        "default": {  
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.environ.get('AZURE_REDIS_CONNECTIONSTRING'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        },
    }
}