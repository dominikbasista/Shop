from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ":memoty:",
    }
}
EMAIL_BACKEND = 'django.core.mail.backens.locmem.EmailBackend'