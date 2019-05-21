from .base import * #NOQA

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeideablog',
        'USER':'root',
        'PASSWORD':123456,
        'HOST':'localhost',
        'PORT':3306,
        'CONN_MAX_AGE':5*60,
        'OPTIONS':{'charset':'utf8mb4'}
    }
}