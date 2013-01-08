from lupeng.settings import *

ADMINS = (
    ('pabe', '19noname19@gmail.com'),
    ('beta', 'mr.bence.tamas@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lupeng_xutt',                      # Or path to database file if using sqlite3.
        'USER': 'globalarts',                      # Not used with sqlite3.
        'PASSWORD': 'globalarts',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEBUG = False
TEMPLATE_DEBUG = False

EMAIL_HOST = 'post.symbler.net'
EMAIL_HOST_USER = 'rop.post'
EMAIL_HOST_PASSWORD = 'riprop'
EMAIL_HOST = '188.40.190.110'

