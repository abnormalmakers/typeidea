from .base import * #NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeideablog',
        'USER':'root',
        'PASSWORD':123456,
        'HOST':'localhost',
        'PORT':3306
    }
}

DEBUG=True