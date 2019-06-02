from .base import * #NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeideablog',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':3306
    }
}

DEBUG=True