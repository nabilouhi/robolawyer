from .base import *

DEBUG = True
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
